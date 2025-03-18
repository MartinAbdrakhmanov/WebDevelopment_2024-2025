var count = 0;
document.getElementById("myButton").onclick = function () {
    count++;
    if (count % 2 == 0) {
        document.getElementById("demo").innerHTML = "";
    } else {
        var img = document.createElement("img");
        img.src = "https://cdn.7tv.app/emote/60f88df431ba6ae622371d8e/4x.webp";
        document.getElementById("demo").appendChild(img);
    }
}


// Функция для показа всплывающего окна
function showPopup(message) {
    const popup = document.getElementById('popup');
    const overlay = document.getElementById('overlay');
    const body = document.body;

    popup.innerHTML = message;
    popup.style.display = 'block';
    overlay.style.display = 'block';
    body.classList.add('popup-active');

    setTimeout(() => {
        popup.style.display = 'none';
        overlay.style.display = 'none';
        body.classList.remove('popup-active');
    }, 3000);
}

// Функция для показа изображения
function showImage(imageSrc) {
    const popup = document.getElementById('popup');
    const overlay = document.getElementById('overlay');
    const body = document.body;

    popup.innerHTML = `<img src="${imageSrc}" alt="Картинка" style="max-width: 100%; height: auto;">`;
    popup.style.display = 'block';
    overlay.style.display = 'block';
    body.classList.add('popup-active');
}

// Функция для воспроизведения музыки
function playMusic(musicSrc) {
    const audio = new Audio(musicSrc);
    audio.volume = 0.5;
    audio.play();
    setTimeout(() => { audio.pause() }, 5000)
}

// Закрытие всплывающего окна при клике на затемнение
document.getElementById('overlay').addEventListener('click', () => {
    const popup = document.getElementById('popup');
    const overlay = document.getElementById('overlay');
    const body = document.body;

    popup.style.display = 'none';
    overlay.style.display = 'none';
    body.classList.remove('popup-active');
});