var images = [], changeImages;

fetch(localStorage.getItem("url_pokemon"))
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    console.log(data);
    let name = data["name"].charAt(0).toUpperCase() + data["name"].slice(1);
    let sprites = Object.values(data["sprites"]);
    images = sprites.filter(item => item != null && typeof(item) == 'string');
    let rows_table = '';
    data["abilities"].map((item, i) => {
      let ability = item["ability"]["name"].charAt(0).toUpperCase() + item["ability"]["name"].slice(1);
      rows_table += `<tr>
        ${ i == 0 ? `<td rowspan="${ data["abilities"].length }"><img id="img_pokemon"></td>` : '' }
        <td>${ ability }</td>
      </tr>`
    });
    document.querySelector("#details_pokemon > thead th.name").innerHTML = name;
    document.querySelector("#details_pokemon > tbody").innerHTML = rows_table;
    let index = 0;
    changeImages = setInterval(function(){
      document.getElementById("img_pokemon").setAttribute("src", images[index]);
      if (index >= images.length-1) { index = 0 }
      else { index++ }
    },700)
  });

