var pivot_pokemons = 1, initial_range = 1;

fetch('https://pokeapi.co/api/v2/pokemon/')
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    setPokemonsTable(data);
    document.getElementById("total_pokemon").innerHTML = data.count;
    document.getElementById("btn_next").setAttribute("onclick",`getPokemon('${data.next}','next')`);
  });

// ------------------------------------------------------------------------
function setPokemonsTable(data) {
  let cells_table = '';
  let rows_table = '';
  let num_results = data["results"].length; 
  data["results"].sort((a, b) => a["name"] < b["name"] ? -1 : (a["name"] > b["name"] ? 1 : 0));    
  data["results"].map((pokemon, i) => {
    cells_table += `<td onclick="cacheURLPokemon('${pokemon.url}')" title="Ver detalles">${pokemon.name.charAt(0).toUpperCase()+pokemon.name.slice(1)}</td>`;
    if ((i+1)%4 == 0 || ((pivot_pokemons == Math.floor(data.count/20)+1) && (i+1) == num_results)) { 
      rows_table += `<tr>${cells_table}</tr>`;
      cells_table = '';
    }
  });
  document.querySelector("#list_pokemon > tbody").innerHTML = rows_table;
  document.getElementById("initial_range").innerHTML = initial_range;
  document.getElementById("final_range").innerHTML = initial_range + num_results - 1;
  document.getElementById("page_table").innerHTML = pivot_pokemons;
  document.getElementById("total_pages").innerHTML = Math.floor(data.count/20)+1;
}

// ------------------------------------------------------------------------
function getPokemon(url, direction) {
  fetch(url)
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    document.getElementById("btn_previous").setAttribute("onclick",`getPokemon('${data.previous}','previous')`);
    document.getElementById("btn_next").setAttribute("onclick",`getPokemon('${data.next}','next')`);
    
    if (data.previous == null) { document.getElementById("btn_previous").setAttribute("disabled","true") }
    else { document.getElementById("btn_previous").removeAttribute("disabled") }

    if (direction == 'next') { pivot_pokemons++ }
    else { pivot_pokemons-- }
    
    if (pivot_pokemons == Math.floor(data.count/20)+1) { document.getElementById("btn_next").setAttribute("disabled","true") }
    else { document.getElementById("btn_next").removeAttribute("disabled") }

    initial_range = pivot_pokemons == 1 ? pivot_pokemons : initial_range + (direction == 'next' ? 20 : -20);
    setPokemonsTable(data);
  });
}

function cacheURLPokemon(url) {
  localStorage.setItem("url_pokemon", url);
  location.href = "/login";
}