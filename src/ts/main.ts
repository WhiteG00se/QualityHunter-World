import fs from "fs"
import { Parser } from "binary-parser"

const inputPath = "src/armor.am_dat"
const outputPath = `${inputPath}.json`

// Define the parser schema
const entryParser = new Parser()
	.uint32le("Index")
	.uint16le("Order")
	.uint8("Variant")
	.uint16le("Set_Layered_Id")
	.uint8("Type")
	.uint8("Equip_Slot")
	.uint16le("Defense")
	.uint16le("Model_Id_1")
	.uint16le("Model_Id_2")
	.uint16le("Icon_Color")
	.uint8("Icon_Effect")
	.uint8("Rarity")
	.uint32le("Cost")
	.int8("Fire_Res")
	.int8("Water_Res")
	.int8("Ice_Res")
	.int8("Thunder_Res")
	.int8("Dragon_Res")
	.uint8("Slot_Count")
	.uint8("Slot_1_Size")
	.uint8("Slot_2_Size")
	.uint8("Slot_3_Size")
	.uint16le("Set_Skill_1")
	.uint8("Set_Skill_1_Level")
	.uint16le("Hidden_Skill")
	.uint8("Hidden_Skill_Level")
	.uint16le("Skill_1")
	.uint8("Skill_1_Level")
	.uint16le("Skill_2")
	.uint8("Skill_2_Level")
	.uint16le("Skill_3")
	.uint8("Skill_3_Level")
	.uint32le("Gender")
	.uint16le("Set_Group")
	.uint16le("GMD_Name_Index")
	.uint16le("GMD_Description_Index")
	.uint8("Is_Permanent")

const headerParser = new Parser()
	.endianess("little")
	.uint32("Magic_1")
	.uint16("Magic_2")
	.uint32("Entry_Count")

// Read the binary file
fs.readFile(inputPath, (err: any, data: Buffer) => {
	if (err) throw err

	// Parse the header
	const header = headerParser.parse(data)

	// Parse the entries
	const entries = []
	let offset = headerParser.sizeOf()
	for (let i = 0; i < header.Entry_Count; i++) {
		const entry = entryParser.parse(data.slice(offset))
		entries.push(entry)
		offset += entryParser.sizeOf()
	}

	// Convert to JSON
	const result = {
		Header: header,
		Entries: entries
	}

	// Write the JSON to a file
	fs.writeFile(outputPath, JSON.stringify(result, null, 2), (err: any) => {
		if (err) throw err
		console.log("Conversion complete. JSON saved to output.json")
	})
})
