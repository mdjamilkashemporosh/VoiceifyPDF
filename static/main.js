const dropArea = document.querySelector(".drop_box"),
  button_choose = dropArea.querySelector("#btn_choose"),
  dragText = dropArea.querySelector("header"),
  input = dropArea.querySelector("input"),
  loading = dropArea.querySelector("#loading");
  action_elements = dropArea.querySelector("#action");
  download_btn = dropArea.querySelector("#download");
  play_btn = dropArea.querySelector("#play");

const URL = "http://127.0.0.1:8000";

let playing = false;

button_choose.onclick = () => {
  input.click();
};

const handleDownload = async (blob) => {
  try {
    playing = true;
    const link = document.createElement("a");
    link.href = window.URL.createObjectURL(blob);
    link.download = "audio.mp3";
    link.click();
    window.URL.revokeObjectURL(link.href);
  } catch (error) {
    console.error(error);
  }
};
const handlePlay = async (blob) => {
  try {
    playing = true;
    audio = new Audio(window.URL.createObjectURL(blob));
    document.body.appendChild(audio);
    audio.play();
    play_btn.textContent = "Pause";
    play_btn.addEventListener("click", () => {
      if (audio.paused) {
        audio.play();
        play_btn.textContent = "Pause";
      } else {
        audio.pause();
        play_btn.textContent = "Play";
      }
    });
    audio.addEventListener("ended", () => {
      playing = false;
      window.URL.revokeObjectURL(audio.src);
      document.body.removeChild(audio);
      document.body.removeChild(pauseButton);
    });
  } catch (error) {
    console.error(error);
  }
};

input.addEventListener("change", function (e) {
  button_choose.classList.add("hidden");
  loading.classList.remove("hidden");

  const formData = new FormData();
  formData.append("file", e.target.files[0]);

  fetch(`${URL}/upload`, {
    method: "POST",
    body: formData,
  })
    .then((response) => response.blob())
    .then((blob) => {
      // Create an audio element
      loading.classList.add("hidden");
      action_elements.classList.remove("hidden");

      download_btn.addEventListener("click", () => {
        handleDownload(blob);
      });
      play_btn.addEventListener("click", () => {
        if (!playing) {
          handlePlay(blob);
        }
      });
    })
    .catch((error) => console.error(error));
});
