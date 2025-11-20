
let center = [0.4102822, 9.4368245];
let map = L.map('map').setView(center, 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
let marker = L.marker(center).addTo(map);
marker.bindPopup('<p><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6JPYDWuAB0WrFVT21wReu7DUDyeHc0I8Vuw&s" alt="WomenGoForPeace" class="w-20 h-auto mb-1"><br>Women Go For Peace</p>').openPopup();
