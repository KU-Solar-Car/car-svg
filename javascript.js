// Grab data from CSV as string.
let csv_string = "";
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
 		parse(this.responseText);
	}
};
xhttp.open("GET", "data.csv", true);
xhttp.send();

// Now parse csv into array of donor objects, the indexes of which will
// correspond to the indexes of the cells.
var donor_list = [];
function parse(csv_string) {
  lines = csv_string.split('\n');
  for(i=1; i < lines.length; i++) {
    cols = lines[i].split(',');
    donor_name = cols[0];
    donor_amount = cols[1];
    donor_cells = cols[2];
    for(let i=0; i < donor_cells; i++) {
      donor_list.push({name: donor_name, amount: donor_amount, cells: donor_cells})
    }
  }
}

var textdiv = document.getElementById("donor-text-box");
textdiv.hidden = true;
var text_elem = document.getElementById('donor-text');

var car = document.getElementById("car");
car.addEventListener('load', (event) => {
  var svg_doc = car.contentDocument;
  cells = svg_doc.getElementsByTagName("polygon");

  for(let i=0; i < cells.length; i++) {
    if(i < donor_list.length) {
      cells[i].addEventListener("mouseover", (event) => {
        var text_to_display = donor_list[i].name + "\n" + donor_list[i].amount;
        text_elem.innerText = text_to_display;
        textdiv.hidden = false;
        cells[i].style.fill = "#e4e4e7"
        console.log("over")
      });
      cells[i].addEventListener("mouseout", (event) => {
        textdiv.hidden = true;
        cells[i].style.fill = "#3b3c3e"
      });
    } else {
      cells[i].style.opacity = "0.7"
    }
  }
});
