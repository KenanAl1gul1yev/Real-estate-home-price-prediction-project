let sqft = document.querySelector("#uiSqft");
let rooms = document.querySelector("#uiRooms");
let floor = document.querySelector("#uiFloor");
let floor2 = document.querySelector("#uiFloor2");
let estPrice = document.querySelector(".submit");
let uiEstimatedPrice = document.querySelector("#uiEstimatedPrice");
;
estPrice.addEventListener("click", function ad(e) {
  e.preventDefault();
  onClickedEstimatePrice();
});
async function onClickedEstimatePrice() {
  let location = document.querySelector("#uiLocations");
  const url = "http://127.0.0.1:5000/predict_apt_price";
  console.log(parseFloat(floor.value / floor2.value));
  console.log(location.value.slice(9));
  console.log("Estimate price button clicked");
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

async function onPageLoad() {
  console.log("document loaded");
  const url = "http://127.0.0.1:5000/get_apt_location_names";
  $.get(url, function (data, status) {
    console.log("got response for get_location_names request");
    if (data) {
      let locations = data.locations;
      $("#uiLocations").empty();
      for (let i in locations) {
        let opt = new Option(locations[i]);
        $("#uiLocations").append(opt);
      }
      $("#uiLocations").append('<option>Diger...</option>');
    }
  });
}

window.onload = onPageLoad;
