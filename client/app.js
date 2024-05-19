let sqft = document.querySelector("#uiSqft");
let rooms = document.querySelector("#uiRooms");
let floor = document.querySelector("#uiFloor");
let floor2 = document.querySelector("#uiFloor2");
let estPrice = document.querySelector(".submit");
let uiEstimatedPrice = document.querySelector("#uiEstimatedPrice");
let changePlace = document.querySelector("#change_place");
let apt_btn = document.querySelector("#change_apart");
let house_btn = document.querySelector("#change_house");

estPrice.addEventListener("click", function ad(e) {
  e.preventDefault();
  if (apt_btn.classList.contains("click_btn")) {
    console.log("apt isledi");
    onClickedEstimatePriceApt();
  } else {
    let groundArea = document.querySelector("#uiGroundArea");
    onClickedEstimatePriceHouse();
  }
});

async function onClickedEstimatePriceApt() {
  let location = document.querySelector("#uiLocations");
  const url = "http://127.0.0.1:5000/predict_apt_price";
  console.log(parseFloat(floor.value / floor2.value));
  console.log(location.value);
  console.log("Estimate price button clicked");
  console.log(sqft.value);
  console.log(rooms.value);
  $.post(
    url,
    {
      area: parseFloat(sqft.value),
      rooms: parseInt(rooms.value, 10),
      floor: parseFloat(floor.value / floor2.value),
      location: location.value,
    },
    function (data, status) {
      console.log(data.estimated_price);
      uiEstimatedPrice.innerHTML =
        "<h2>" + data.estimated_price.toString() + " AZN</h2>";
      console.log(status);
    }
  );
}

async function onClickedEstimatePriceHouse() {
  let groundArea = document.querySelector("#uiGroundArea");
  let location = document.querySelector("#uiLocations");
  const url = "http://127.0.0.1:5000/predict_house_price";
  console.log(location.value);
  console.log("Estimate price button clicked");
  $.post(
    url,
    {
      area: parseFloat(sqft.value),
      rooms: parseInt(rooms.value, 10),
      groundArea: parseFloat(groundArea.value),
      location: location.value,
    },
    function (data, status) {
      console.log(data.estimated_price);
      uiEstimatedPrice.innerHTML =
        "<h2>" + data.estimated_price.toString() + " AZN</h2>";
      console.log(status);
    }
  );
}

function clear_values() {
  uiEstimatedPrice.innerHTML = "";
  sqft.value = "";
  rooms.value = "";
}

house_btn.addEventListener("click", function (e) {
  e.preventDefault();
  apt_btn.classList.remove("click_btn");
  house_btn.classList.add("click_btn");
  changePlace.innerHTML =
    '<h2>Ground Area</h2> <input class="area" type="text" id="uiGroundArea" name="GroundArea" placeholder="exp: 6"/>';
  onPageLoadHouse();
  clear_values();
});

apt_btn.addEventListener("click", function (e) {
  e.preventDefault();
  house_btn.classList.remove("click_btn");
  apt_btn.classList.add("click_btn");
  changePlace.innerHTML =
    '<h2>Floor(Apartment located)</h2> <input class="area floatLabel" type="text" id="uiFloor" name="Floor" placeholder="exp: 5" /> <h2>Floor(Building have)</h2> <input class="area floatLabel" type="text" id="uiFloor2" name="Floor2" placeholder="exp: 17" />';
  onPageLoadApt();
  clear_values();
});

async function onPageLoadApt() {
  console.log("document loaded");
  const url = "http://127.0.0.1:5000/get_apt_location_names";
  $.get(url, function (data, status) {
    console.log("got response for get_apt_location_names request");
    if (data) {
      let locations = data.locations;
      $("#uiLocations").empty();
      $("#uiLocations").selectpicker("refresh");
      for (let i in locations) {
        let opt = new Option(locations[i]);
        $("#uiLocations").append(opt);
        $("#uiLocations").selectpicker("refresh");
      }
      $("#uiLocations").append("<option>Diger...</option>");
      $("#uiLocations").selectpicker("refresh");
    }
  });
}

async function onPageLoadHouse() {
  console.log("document loaded");
  const url = "http://127.0.0.1:5000/get_house_location_names";
  $.get(url, function (data, status) {
    console.log("got response for get_house_location_names request");
    if (data) {
      let locations = data.locations;
      $("#uiLocations").empty();
      $("#uiLocations").selectpicker("refresh");
      for (let i in locations) {
        let opt = new Option(locations[i]);
        $("#uiLocations").append(opt);
        $("#uiLocations").selectpicker("refresh");
      }
      $("#uiLocations").append("<option>Diger...</option>");
      $("#uiLocations").selectpicker("refresh");
    }
  });
}

window.onload = onPageLoadApt;


$(function () {
  $(".selectpicker").selectpicker();
});