import frappe
from erpnext.manufacturing.doctype.job_card.job_card import JobCard
from frappe.utils import flt, get_link_to_form


class InventoryToolsJobCard(JobCard):
	def validate_job_card_qty(self):
		if not (self.operation_id and self.work_order):
			return
		bypass_qty_validation = frappe.db.get_value(
			"Inventory Tools Settings", self.company, "bypass_qty_validation"
		)
		if self.docstatus != 1 and bypass_qty_validation:
			return

		wo_qty = flt(frappe.get_cached_value("Work Order", self.work_order, "qty"))

		completed_qty = flt(
			frappe.db.get_value("Work Order Operation", self.operation_id, "completed_qty")
		)

		over_production_percentage = flt(
			frappe.db.get_single_value("Manufacturing Settings", "overproduction_percentage_for_work_order")
		)

		wo_qty = wo_qty + (wo_qty * over_production_percentage / 100)

		job_card_qty = frappe.get_all(
			"Job Card",
			fields=["sum(for_quantity)"],
			filters={
				"work_order": self.work_order,
				"operation_id": self.operation_id,
				"docstatus": ["!=", 2],
			},
			as_list=1,
		)

		job_card_qty = flt(job_card_qty[0][0]) if job_card_qty else 0

		if job_card_qty and ((job_card_qty - completed_qty) > wo_qty):
			form_link = get_link_to_form("Manufacturing Settings", "Manufacturing Settings")

			msg = f"""
				Qty To Manufacture in the job card
				cannot be greater than Qty To Manufacture in the
				work order for the operation {frappe.bold(self.operation)}.
				<br><br><b>Solution: </b> Either you can reduce the
				Qty To Manufacture in the job card or set the
				'Overproduction Percentage For Work Order'
				in the {form_link}."""

			frappe.throw(frappe._(msg), title=frappe._("Extra Job Card Quantity"))
