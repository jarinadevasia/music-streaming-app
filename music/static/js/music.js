<script>
var audio = document.getElementById("myAudio");
var progress = document.querySelector(".progress");

function playAudio() {
  audio.play();
}

function pauseAudio() {
  audio.pause();
}

audio.addEventListener("timeupdate", function() {
  var currentTime = audio.currentTime;
  var duration = audio.duration;
  var progressWidth = (currentTime / duration) * 100 + "%";
  progress.style.width = progressWidth;
});

audio.addEventListener("ended", function() {
  progress.style.width = "0";
});
</script>