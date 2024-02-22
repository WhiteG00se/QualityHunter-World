const fs = require("fs")
const readline = require("readline")

const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
})

rl.question("Enter the full path of the CSV file: ", (csvFilePath) => {
	rl.close()
	generatePatchJson(csvFilePath)
})

function generatePatchJson(csvFilePath) {
	const targetFile = "armor.am_dat"
	const version = 3
	const changes = { Entries: {} }

	const csvData = fs.readFileSync(csvFilePath, "utf8").split("\n")
	const headers = csvData.shift().trim().split("|")

	csvData.forEach((line) => {
		const values = line.trim().split("|")
		const entry = {}
		headers.forEach((header, index) => {
			if (header && values[index]) {
				entry[header] = values[index]
			}
		})

		const key = `${entry["P1_Set_Group"]}|${entry["p2_Variant"]}|${entry["P3_Type"]}|${entry["P4_Equip_slot"]}`
		if (!changes.Entries[key]) {
			changes.Entries[key] = {}
		}
		changes.Entries[key]["Defense"] = parseInt(entry["col6"])
	})

	const patchData = {
		targetFile,
		version,
		changesV3: changes
	}

	const patchJson = JSON.stringify(patchData, null, 2)
	const scriptDir = __dirname
	const outputPath = `${scriptDir}/patch.json`
	fs.writeFileSync(outputPath, patchJson)
	console.log(`Patch JSON file has been saved to: ${outputPath}`)
}
