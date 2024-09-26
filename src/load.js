async function main() {
    let url = "./src/data.json"
    let json = await fetch(url).then((response) => response.json())

    console.log(json)
    console.log(json.table.headers)
    populateTable(json.table)
}

function populateTable(json) {
    let table = document.getElementById("table")

    // Set headers
    let header_row = document.createElement("tr")
    table.appendChild(header_row)

    for (header of json['headers']) {
        let header_cell = document.createElement("th")
        header_cell.innerText = header
        header_row.appendChild(header_cell)
    }

    // Set rows
    for (index in json['rows']) {
        let row = json['rows'][index]
        let row_element = document.createElement("tr")
        table.appendChild(row_element)

        for (value of row) {
            let cell = document.createElement("th")
            cell.innerText = value
            row_element.appendChild(cell)
        }
    }   
}
    
main()