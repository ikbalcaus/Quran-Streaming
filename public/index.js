const audio = new Audio();
const preloadedAudio = new Audio();
let surahNo;
let ayahNo;
let totalAyah;
let preloadedData = {};

function start() {
    document.getElementById("startup").style.display = "none";
    fetch("https://quranapi.pages.dev/api/{{data.surah}}/{{data.ayah}}.json")
    .then((response) => response.json())
    .then((data) => {
        surahNo = data.surahNo;
        ayahNo = data.ayahNo;
        totalAyah = data.totalAyah;
        document.getElementById("title").innerText = `${data.surahName} (${data.surahNo}:${data.ayahNo})`;
        document.getElementById("text").innerText = data.english;
        audio.src = `https://quranaudio.pages.dev/1/${surahNo}_${ayahNo}.mp3`;
        audio.play();
        preload();
    })
    .catch((error) => console.error("Error:", error));
}

function preload() {
    ayahNo++;
    if (ayahNo > totalAyah) {
        ayahNo = 1;
        surahNo++;
    }
    if (surahNo > 114) {
        surahNo = 1;
    }
    fetch(`https://quranapi.pages.dev/api/${surahNo}/${ayahNo}.json`)
    .then((response) => response.json())
    .then((data) => {
        preloadedData = data;
        preloadedAudio.src = `https://quranaudio.pages.dev/1/${surahNo}_${ayahNo}.mp3`;
        preloadedAudio.load();
    })
    .catch((error) => console.error("Error:", error));
}

function next() {
    document.getElementById("title").innerText = `${preloadedData.surahName} (${surahNo}:${ayahNo})`;
    document.getElementById("text").innerText = preloadedData.english;
    audio.src = preloadedAudio.src;
    audio.play();
    preload();
}

audio.addEventListener("ended", next);
