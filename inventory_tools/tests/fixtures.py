suppliers = [
	(
		"Freedom Provisions",
		None,
		None,
		None,
		"Net 30",
		{
			"address_line1": "16 Margrave",
			"city": "Carlisle",
			"state": "NH",
			"country": "United States",
			"pincode": "57173",
		},
	),
	(
		"Unity Bakery Supply",
		None,
		None,
		None,
		"Net 30",
		{
			"address_line1": "34 Pinar St",
			"city": "Unity",
			"state": "RI",
			"country": "United States",
			"pincode": "34291",
		},
	),
	(
		"Chelsea Fruit Co",
		None,
		None,
		None,
		"Net 30",
		{
			"address_line1": "67C Sweeny Street",
			"city": "Chelsea",
			"state": "MA",
			"country": "United States",
			"pincode": "89077",
		},
	),
	(
		"Credible Contract Baking",
		None,
		None,
		None,
		"Net 30",
		{
			"address_line1": "4 Crumb Circle",
			"city": "Belmont",
			"state": "MA",
			"country": "United States",
			"pincode": "89074",
		},
	),
]

workstations = [
	("Mix Pie Crust Station", "20"),
	("Roll Pie Crust Station", "20"),
	("Make Pie Filling Station", "20"),
	("Cooling Station", "100"),
	("Box Pie Station", "100"),
	("Baking Station", "20"),
	("Assemble Pie Station", "20"),
	("Mix Pie Filling Station", "20"),
	("Packaging Station", "2"),
	("Food Prep Table 2", "10"),
	("Food Prep Table 1", "5"),
	("Range Station", "20"),
	("Cooling Racks Station", "80"),
	("Refrigerator Station", "200"),
	("Oven Station", "20"),
	("Mixer Station", "10"),
]

operations = [
	(
		"Gather Pie Crust Ingredients",
		"Food Prep Table 2",
		"5",
		"""- Remove flour, salt, and a pie tins from store room
	- Remove butter and ice water from refrigerator
	- Place ingredients at workstation
	- Measure amounts for batch size into mixing bowl""",
	),
	(
		"Gather Pie Filling Ingredients",
		"Food Prep Table 1",
		"5",
		"""- Remove fruit and butter from refrigerator
	- Remove sugar and cornstarch
	- Get water from sink
	- Measure ingredients and place in pot, excluding 1/4 of fruit and butter""",
	),
	(
		"Assemble Pie Op",
		"Food Prep Table 2",
		"5",
		"""- Use fresh pie filling or remove from refrigerator
	- Remove rolled pie crusts from refrigerator
	- Fill bottom crust with filling
	- Create decorative cut out for top crust
	- Layer top crust over bottom crust / filling and create a crimped seal""",
	),
	(
		"Cook Pie Filling Operation",
		"Range Station",
		"5",
		"""- Bring ingredients to simmer and cook for 15 minutes
	- Remove from heat and mix in remaining 1/4 berries and butter
	- Store in refrigerator if not using immediately""",
	),
	(
		"Mix Pie Crust Op",
		"Mixer Station",
		"5",
		"""- Combine flour, butter, salt, and ice water in mixer
	- Pulse for 30 seconds
	- Divide into equal-sized portions, one portion for each pie crust being made
	- Put in refrigerator""",
	),
	("Box Pie Op", "Packaging Station", "5", "- Place pie into box for sale"),
	(
		"Roll Pie Crust Op",
		"Food Prep Table 2",
		"5",
		"""- Remove chilled pie crust portions from refrigerator
	- Separate each portion into two (one for bottom crust, one for top)
	- Flour board and roll out each portion into a circle
	- Place bottom crust into pie tin, then layer a piece of parchment paper, followed by the top crust""",
	),
	("Divide Dough Op", "Food Prep Table 2", "1", "Divide Dough Op"),
	(
		"Bake Op",
		"Oven Station",
		"1",
		"""- Place assembled pies into oven
	- Bake at 375F for 50 minutes
	- Remove from oven""",
	),
	("Chill Pie Crust Op", "Refrigerator Station", "1", "- Chill pie crust for at least 30 minutes"),
	(
		"Cool Pie Op",
		"Cooling Racks Station",
		"1",
		"Cool baked pies for at least 30 minutes before boxing",
	),
]

items = [
	{
		"item_code": "Ambrosia Pie",
		"item_group": "Baked Goods",
		"uom": "Nos",
		"item_price": 11.00,
		"default_warehouse": "Refrigerated Display - APC",
		"description": "<div><p>Ambrosia Pie is the marquee product of Ambrosia Pie Company. A filling of heavenly cloudberries pair perfectly with the tart hairless rambutan, finished with drizzles of tayberry nectar. It's a feast fit for Mt Olympus!</p></div>",
	},
	{
		"item_code": "Double Plum Pie",
		"uom": "Nos",
		"item_group": "Baked Goods",
		"item_price": 10.50,
		"default_warehouse": "Refrigerated Display - APC",
		"description": "<div><p>Double the fun and double the flavor with our Double Plum Pie! We combine damson and cocoplums in a daring tropical-meets-temperate filling. Forbidden fruit never tasted this good.</p></div>",
	},
	{
		"item_code": "Gooseberry Pie",
		"uom": "Nos",
		"item_group": "Baked Goods",
		"item_price": 12.00,
		"default_warehouse": "Refrigerated Display - APC",
		"description": "<div><p>Our delicious take on the traditional gooseberry pie that tastes like the holidays. This classic pie is best shared with the ones you love.</p></div>",
	},
	{
		"item_code": "Kaduka Key Lime Pie",
		"item_group": "Baked Goods",
		"uom": "Nos",
		"item_price": 11.50,
		"default_warehouse": "Refrigerated Display - APC",
		"description": "<div><p>Take your tastebuds on an adventure with this whimsical twist on the classic Key Lime pie. Made with kaduka limes and the exotic limequat, this seasonal pie is sure to satisfy even the most weary culinary explorer. Grab it when you can - it's only available April through September.</p></div>",
	},
	{
		"item_code": "Ambrosia Pie Filling",
		"uom": "Cup",
		"item_group": "Sub Assemblies",
		"default_warehouse": "Refrigerator - APC",
		"description": "Ambrosia Pie Filling",
	},
	{
		"item_code": "Double Plum Pie Filling",
		"uom": "Cup",
		"item_group": "Sub Assemblies",
		"default_warehouse": "Refrigerator - APC",
		"description": "Double Plum Pie Filling",
	},
	{
		"item_code": "Gooseberry Pie Filling",
		"uom": "Cup",
		"description": "Gooseberry Pie Filling",
		"item_group": "Sub Assemblies",
		"default_warehouse": "Refrigerator - APC",
	},
	{
		"item_code": "Kaduka Key Lime Pie Filling",
		"item_group": "Sub Assemblies",
		"default_warehouse": "Refrigerator - APC",
		"uom": "Cup",
		"description": "Kaduka Key Lime Pie Filling",
	},
	{
		"item_code": "Pie Crust",
		"uom": "Nos",
		"description": "Pie Crust",
		"item_group": "Sub Assemblies",
		"default_warehouse": "Refrigerator - APC",
		"is_sub_contracted_item": 1,
		"item_price": 2.00,
		"default_supplier": "",
		"supplier": "",
		"valuation_rate": 3.0196,
		"uom_conversion_detail": {"Hour": 20},
	},
	{
		"item_code": "Pie Crust Service per Crust",
		"uom": "Nos",
		"description": "Subcontracted pie crust manufacturing service. Item price is per crust.",
		"item_group": "Sub Assemblies",
		"default_warehouse": "Credible Contract Baking - APC",
		"is_sub_contracted_item": 1,
		"is_stock_item": 0,
		"item_price": 2.00,
		"default_supplier": "Credible Contract Baking",
		"supplier": "Credible Contract Baking",
	},
	{
		"item_code": "Pie Crust Service per Hour",
		"uom": "Hour",
		"description": "Subcontracted pie crust manufacturing service. Item price is per hour.",
		"item_group": "Sub Assemblies",
		"default_warehouse": "Credible Contract Baking - APC",
		"is_sub_contracted_item": 1,
		"is_stock_item": 0,
		"item_price": 40.00,  # Assumes 5 crusts takes 15 mins (excluding chilling time), or 20 crusts/hour at rate of $2.00/crust
		"default_supplier": "Credible Contract Baking",
		"supplier": "Credible Contract Baking",
	},
	{
		"item_code": "Cloudberry",
		"uom": "Pound",
		"description": "Our Own Cloudberry",
		"item_group": "Ingredients",
		"item_price": 0.65,
		"default_warehouse": "Refrigerator - APC",
		"supplier": "Chelsea Fruit Co",
	},
	{
		"item_code": "Cocoplum",
		"uom": "Pound",
		"description": "Cocoplum",
		"item_group": "Ingredients",
		"item_price": 0.35,
		"default_warehouse": "Refrigerator - APC",
		"supplier": "Chelsea Fruit Co",
	},
	{
		"item_code": "Damson Plum",
		"uom": "Pound",
		"description": "Damson Plum",
		"item_group": "Ingredients",
		"item_price": 0.85,
		"default_warehouse": "Refrigerator - APC",
		"supplier": "Chelsea Fruit Co",
	},
	{
		"item_code": "Gooseberry",
		"uom": "Pound",
		"description": "Gooseberry",
		"item_group": "Ingredients",
		"item_price": 0.99,
		"default_warehouse": "Refrigerator - APC",
		"supplier": "Chelsea Fruit Co",
	},
	{
		"item_code": "Hairless Rambutan",
		"uom": "Pound",
		"description": "Hairless Rambutan",
		"item_price": 0.50,
		"item_group": "Ingredients",
		"default_warehouse": "Storeroom - APC",
		"supplier": "Chelsea Fruit Co",
	},
	{
		"item_code": "Kaduka Lime",
		"uom": "Pound",
		"description": "Kaduka Lime",
		"item_group": "Ingredients",
		"item_price": 0.89,
		"default_warehouse": "Refrigerator - APC",
		"supplier": "Chelsea Fruit Co",
	},
	{
		"item_code": "Limequat",
		"uom": "Pound",
		"description": "Limequat",
		"item_group": "Ingredients",
		"item_price": 0.75,
		"default_warehouse": "Refrigerator - APC",
		"supplier": "Chelsea Fruit Co",
	},
	{
		"item_code": "Tayberry",
		"uom": "Pound",
		"description": "Tayberry - Box",
		"item_group": "Ingredients",
		"item_price": 0.85,
		"default_warehouse": "Refrigerator - APC",
		"supplier": "Chelsea Fruit Co",
	},
	{
		"item_code": "Butter",
		"uom": "Pound",
		"description": "Butter",
		"item_group": "Ingredients",
		"item_price": 4.5,
		"default_warehouse": "Refrigerator - APC",
		"supplier": "Freedom Provisions",
	},
	{
		"item_code": "Cornstarch",
		"uom": "Pound",
		"description": "Cornstarch",
		"item_group": "Ingredients",
		"item_price": 0.52,
		"default_warehouse": "Storeroom - APC",
		"supplier": "Freedom Provisions",
	},
	{
		"item_code": "Ice Water",
		"uom": "Cup",
		"description": "Ice Water - necessary for pie crusts",
		"item_group": "Ingredients",
		"item_price": 0.01,
		"default_warehouse": "Refrigerator - APC",
		"available_in_house": 1,
		"opening_qty": 50,
	},
	{
		"item_code": "Flour",
		"uom": "Pound",
		"description": "Flour",
		"item_group": "Ingredients",
		"item_price": 0.66,
		"default_warehouse": "Storeroom - APC",
		"supplier": "Freedom Provisions",
	},
	{
		"item_code": "Pie Box",
		"uom": "Nos",
		"description": "Pie Box",
		"item_group": "Bakery Supplies",
		"item_price": 0.4,
		"default_warehouse": "Storeroom - APC",
		"supplier": ["Freedom Provisions", "Unity Bakery Supply"],
	},
	{
		"item_code": "Pie Tin",
		"uom": "Nos",
		"description": "Pie Tin",
		"item_price": 0.18,
		"item_group": "Bakery Supplies",
		"default_warehouse": "Storeroom - APC",
		"supplier": ["Freedom Provisions", "Unity Bakery Supply"],
	},
	{
		"item_code": "Parchment Paper",
		"uom": "Nos",
		"description": "Parchment Paper",
		"item_group": "Bakery Supplies",
		"item_price": 0.02,
		"default_warehouse": "Storeroom - APC",
		"supplier": ["Freedom Provisions", "Unity Bakery Supply"],
	},
	{
		"item_code": "Salt",
		"uom": "Pound",
		"description": "Salt",
		"item_group": "Ingredients",
		"item_price": 0.36,
		"default_warehouse": "Storeroom - APC",
		"supplier": "Freedom Provisions",
	},
	{
		"item_code": "Sugar",
		"uom": "Pound",
		"description": "Sugar",
		"item_group": "Ingredients",
		"item_price": 0.60,
		"default_warehouse": "Storeroom - APC",
		"supplier": "Freedom Provisions",
	},
	{
		"item_code": "Water",
		"uom": "Cup",
		"item_price": 0.05,
		"description": "Water",
		"item_group": "Ingredients",
		"default_warehouse": "Kitchen - APC",
		"available_in_house": 1,
		"opening_qty": 50,
	},
]

boms = [
	{
		"item": "Double Plum Pie",
		"quantity": 5.0,
		"uom": "Nos",
		"items": [
			{"item_code": "Pie Crust", "qty": 5.0, "qty_consumed_per_unit": 1.0, "uom": "Nos"},
			{
				"item_code": "Double Plum Pie Filling",
				"qty": 20.0,
				"qty_consumed_per_unit": 4.0,
				"uom": "Cup",
			},
			{"item_code": "Pie Box", "qty": 5.0, "qty_consumed_per_unit": 1.0, "uom": "Nos"},
		],
		"operations": [
			{
				"batch_size": 5,
				"operation": "Assemble Pie Op",
				"time_in_mins": 10.0,
				"workstation": "Food Prep Table 2",
			},
			{"batch_size": 1, "operation": "Bake Op", "time_in_mins": 50.0, "workstation": "Oven Station"},
			{
				"batch_size": 1,
				"operation": "Cool Pie Op",
				"time_in_mins": 30.0,
				"workstation": "Cooling Racks Station",
			},
			{
				"batch_size": 5,
				"operation": "Box Pie Op",
				"time_in_mins": 5.0,
				"workstation": "Packaging Station",
			},
		],
	},
	{
		"item": "Kaduka Key Lime Pie",
		"quantity": 5.0,
		"uom": "Nos",
		"items": [
			{"item_code": "Pie Crust", "qty": 5.0, "qty_consumed_per_unit": 1.0, "uom": "Nos"},
			{
				"item_code": "Kaduka Key Lime Pie Filling",
				"qty": 20.0,
				"qty_consumed_per_unit": 4.0,
				"uom": "Cup",
			},
			{"item_code": "Pie Box", "qty": 5.0, "qty_consumed_per_unit": 1.0, "uom": "Nos"},
		],
		"operations": [
			{
				"batch_size": 5,
				"operation": "Assemble Pie Op",
				"time_in_mins": 10.0,
				"workstation": "Food Prep Table 2",
			},
			{"batch_size": 1, "operation": "Bake Op", "time_in_mins": 50.0, "workstation": "Oven Station"},
			{
				"batch_size": 1,
				"operation": "Cool Pie Op",
				"time_in_mins": 30.0,
				"workstation": "Cooling Racks Station",
			},
			{
				"batch_size": 5,
				"operation": "Box Pie Op",
				"time_in_mins": 5.0,
				"workstation": "Packaging Station",
			},
		],
	},
	{
		"item": "Gooseberry Pie",
		"quantity": 5.0,
		"uom": "Nos",
		"items": [
			{"item_code": "Pie Crust", "qty": 5.0, "qty_consumed_per_unit": 1.0, "uom": "Nos"},
			{
				"item_code": "Gooseberry Pie Filling",
				"qty": 20.0,
				"qty_consumed_per_unit": 4.0,
				"uom": "Cup",
			},
			{"item_code": "Pie Box", "qty": 5.0, "qty_consumed_per_unit": 1.0, "uom": "Nos"},
		],
		"operations": [
			{
				"batch_size": 5,
				"operation": "Assemble Pie Op",
				"time_in_mins": 10.0,
				"workstation": "Food Prep Table 2",
			},
			{"batch_size": 1, "operation": "Bake Op", "time_in_mins": 50.0, "workstation": "Oven Station"},
			{
				"batch_size": 1,
				"operation": "Cool Pie Op",
				"time_in_mins": 30.0,
				"workstation": "Cooling Racks Station",
			},
			{
				"batch_size": 5,
				"operation": "Box Pie Op",
				"time_in_mins": 5.0,
				"workstation": "Packaging Station",
			},
		],
	},
	{
		"item": "Ambrosia Pie",
		"quantity": 5.0,
		"uom": "Nos",
		"items": [
			{"item_code": "Pie Crust", "qty": 5.0, "qty_consumed_per_unit": 1.0, "uom": "Nos"},
			{"item_code": "Ambrosia Pie Filling", "qty": 20.0, "qty_consumed_per_unit": 4.0, "uom": "Cup"},
			{"item_code": "Pie Box", "qty": 5.0, "qty_consumed_per_unit": 1.0, "uom": "Nos"},
		],
		"operations": [
			{
				"batch_size": 5,
				"operation": "Assemble Pie Op",
				"time_in_mins": 10.0,
				"workstation": "Food Prep Table 2",
			},
			{"batch_size": 1, "operation": "Bake Op", "time_in_mins": 50.0, "workstation": "Oven Station"},
			{
				"batch_size": 1,
				"operation": "Cool Pie Op",
				"time_in_mins": 30.0,
				"workstation": "Cooling Racks Station",
			},
			{
				"batch_size": 5,
				"operation": "Box Pie Op",
				"time_in_mins": 5.0,
				"workstation": "Packaging Station",
			},
		],
	},
	{
		"item": "Double Plum Pie Filling",
		"quantity": 20.0,
		"uom": "Cup",
		"items": [
			{"item_code": "Sugar", "qty": 0.5, "qty_consumed_per_unit": 0.025, "uom": "Pound"},
			{"item_code": "Cornstarch", "qty": 0.1, "qty_consumed_per_unit": 0.005, "uom": "Pound"},
			{"item_code": "Water", "qty": 1.25, "qty_consumed_per_unit": 0.0625, "uom": "Cup"},
			{"item_code": "Butter", "qty": 0.313, "qty_consumed_per_unit": 0.01565, "uom": "Pound"},
			{"item_code": "Cocoplum", "qty": 7.5, "qty_consumed_per_unit": 0.02515, "uom": "Pound"},
			{"item_code": "Damson Plum", "qty": 7.5, "qty_consumed_per_unit": 0.02515, "uom": "Pound"},
		],
		"operations": [
			{
				"batch_size": 5,
				"operation": "Gather Pie Filling Ingredients",
				"time_in_mins": 5.0,
				"workstation": "Food Prep Table 1",
			},
			{
				"batch_size": 5,
				"operation": "Cook Pie Filling Operation",
				"time_in_mins": 15.0,
				"workstation": "Range Station",
			},
		],
	},
	{
		"item": "Kaduka Key Lime Pie Filling",
		"quantity": 20.0,
		"uom": "Cup",
		"items": [
			{"item_code": "Sugar", "qty": 0.5, "qty_consumed_per_unit": 0.025, "uom": "Pound"},
			{"item_code": "Cornstarch", "qty": 0.1, "qty_consumed_per_unit": 0.005, "uom": "Pound"},
			{"item_code": "Water", "qty": 1.25, "qty_consumed_per_unit": 0.0625, "uom": "Cup"},
			{"item_code": "Butter", "qty": 0.313, "qty_consumed_per_unit": 0.01565, "uom": "Pound"},
			{"item_code": "Kaduka Lime", "qty": 10.0, "qty_consumed_per_unit": 0.0335, "uom": "Pound"},
			{"item_code": "Limequat", "qty": 5.0, "qty_consumed_per_unit": 0.01675, "uom": "Pound"},
		],
		"operations": [
			{
				"batch_size": 5,
				"operation": "Gather Pie Filling Ingredients",
				"time_in_mins": 5.0,
				"workstation": "Food Prep Table 1",
			},
			{
				"batch_size": 5,
				"operation": "Cook Pie Filling Operation",
				"time_in_mins": 15.0,
				"workstation": "Range Station",
			},
		],
	},
	{
		"item": "Gooseberry Pie Filling",
		"quantity": 20.0,
		"uom": "Cup",
		"items": [
			{"item_code": "Sugar", "qty": 0.5, "qty_consumed_per_unit": 0.025, "uom": "Pound"},
			{"item_code": "Cornstarch", "qty": 0.1, "qty_consumed_per_unit": 0.005, "uom": "Pound"},
			{"item_code": "Water", "qty": 1.25, "qty_consumed_per_unit": 0.0625, "uom": "Cup"},
			{"item_code": "Butter", "qty": 0.313, "qty_consumed_per_unit": 0.01565, "uom": "Pound"},
			{"item_code": "Gooseberry", "qty": 15.0, "qty_consumed_per_unit": 0.05025, "uom": "Pound"},
		],
		"operations": [
			{
				"batch_size": 5,
				"operation": "Gather Pie Filling Ingredients",
				"time_in_mins": 5.0,
				"workstation": "Food Prep Table 1",
			},
			{
				"batch_size": 5,
				"operation": "Cook Pie Filling Operation",
				"time_in_mins": 15.0,
				"workstation": "Range Station",
			},
		],
	},
	{
		"item": "Ambrosia Pie Filling",
		"quantity": 20.0,
		"uom": "Cup",
		"items": [
			{"item_code": "Sugar", "qty": 0.5, "qty_consumed_per_unit": 0.025, "uom": "Pound"},
			{"item_code": "Cornstarch", "qty": 0.1, "qty_consumed_per_unit": 0.005, "uom": "Pound"},
			{"item_code": "Butter", "qty": 0.313, "qty_consumed_per_unit": 0.01565, "uom": "Pound"},
			{
				"item_code": "Hairless Rambutan",
				"qty": 5.0,
				"qty_consumed_per_unit": 0.01675,
				"uom": "Pound",
			},
			{"item_code": "Tayberry", "qty": 2.5, "qty_consumed_per_unit": 0.0084, "uom": "Pound"},
			{"item_code": "Cloudberry", "qty": 7.5, "qty_consumed_per_unit": 0.02515, "uom": "Pound"},
			{"item_code": "Water", "qty": 1.25, "qty_consumed_per_unit": 0.0625, "uom": "Cup"},
		],
		"operations": [
			{
				"batch_size": 5,
				"operation": "Gather Pie Filling Ingredients",
				"time_in_mins": 5.0,
				"workstation": "Food Prep Table 1",
			},
			{
				"batch_size": 5,
				"operation": "Cook Pie Filling Operation",
				"time_in_mins": 15.0,
				"workstation": "Range Station",
			},
		],
	},
	{
		"item": "Pie Crust",  # Subcontracted BOM
		"quantity": 5.0,
		"uom": "Nos",
		"is_default": 0,
		"is_subcontracted": 1,
		"with_operations": 0,
		"items": [
			{"item_code": "Flour", "qty": 4.25, "qty_consumed_per_unit": 0.85, "uom": "Pound"},
			{"item_code": "Butter", "qty": 2.5, "qty_consumed_per_unit": 0.5, "uom": "Pound"},
			# {"item_code": "Ice Water", "qty": 2.5, "qty_consumed_per_unit": 0.5, "uom": "Cup"},
			{"item_code": "Salt", "qty": 0.05, "qty_consumed_per_unit": 0.01, "uom": "Pound"},
			{"item_code": "Parchment Paper", "qty": 5.0, "qty_consumed_per_unit": 1.0, "uom": "Nos"},
			{"item_code": "Pie Tin", "qty": 5.0, "qty_consumed_per_unit": 1.0, "uom": "Nos"},
		],
		"operations": [],  # Subcontracted item -> operations done by supplier
	},
	{
		"item": "Pie Crust",  # In-house BOM
		"quantity": 5.0,
		"uom": "Nos",
		"items": [
			{"item_code": "Flour", "qty": 4.25, "qty_consumed_per_unit": 0.85, "uom": "Pound"},
			{"item_code": "Butter", "qty": 2.5, "qty_consumed_per_unit": 0.5, "uom": "Pound"},
			{"item_code": "Ice Water", "qty": 2.5, "qty_consumed_per_unit": 0.5, "uom": "Cup"},
			{"item_code": "Salt", "qty": 0.05, "qty_consumed_per_unit": 0.01, "uom": "Pound"},
			{"item_code": "Parchment Paper", "qty": 5.0, "qty_consumed_per_unit": 1.0, "uom": "Nos"},
			{"item_code": "Pie Tin", "qty": 5.0, "qty_consumed_per_unit": 1.0, "uom": "Nos"},
		],
		"operations": [
			{
				"batch_size": 5,
				"operation": "Gather Pie Crust Ingredients",
				"time_in_mins": 5.0,
				"workstation": "Food Prep Table 2",
			},
			{
				"batch_size": 5,
				"operation": "Mix Pie Crust Op",
				"time_in_mins": 5.0,
				"workstation": "Mixer Station",
			},
			{
				"batch_size": 1,
				"operation": "Divide Dough Op",
				"time_in_mins": 2.0,
				"workstation": "Food Prep Table 2",
			},
			{
				"batch_size": 1,
				"operation": "Chill Pie Crust Op",
				"time_in_mins": 30.0,
				"workstation": "Refrigerator Station",
			},
			{
				"batch_size": 5,
				"operation": "Roll Pie Crust Op",
				"time_in_mins": 10.0,
				"workstation": "Food Prep Table 2",
			},
		],
	},
]

customers = [
	"Almacs Food Group",
	"Beans and Dreams Roasters",
	"Cafe 27 Cafeteria",
	"Capital Grille Restaurant Group",
	"Downtown Deli",
	"Draws Groceries",
	"Grab n Go Bodega",
	"Grand North Station Baking Co",
	"Happy Basket Food Distribution Group",
	"Jitter Cafe",
	"Longwoods Sandwich Shop",
	"Midtown Munchies Inc",
	"My Way Cup Coffee",
	"Nom Nom Cafe",
	"Round the World Donut Shop",
	"Sand Street Deli",
	"Starfood Cafe",
	"Terrywood Terminal Bakery Inc",
	"TransAmerica Bank Cafeteria",
	"Whole Harvest Grocery Group",
]
