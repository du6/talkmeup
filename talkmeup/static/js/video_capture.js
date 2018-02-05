var cameraStream;

function hasGetUserMedia() {
  return !!(navigator.getUserMedia || navigator.webkitGetUserMedia ||
            navigator.mozGetUserMedia || navigator.msGetUserMedia);
}


if (hasGetUserMedia()) {
    var constraints = {audio: false, video: {width: {ideal: 480}, height: {ideal: 360}}};
    var video = document.querySelector("video");
    var count = 30;
    const record = document.getElementById('record');
    const stop = document.getElementById('stop');
    const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    function successCallback(stream) {
      window.stream = stream; // stream available to console
        if (window.URL) {
            video.src = window.URL.createObjectURL(stream);
        } else {
            video.src = stream;
        }

        //save it for later
        cameraStream = stream;

        video.play();
        var counter = setInterval(function () {
            count = count - 1;
            document.getElementById("timer").innerHTML = count; // watch for spelling
            if (count == 0) {
                stopWebCam();
                clearInterval(counter);
            }
        }, 1000);
    }

    function errorCallback(error) {
      console.log("navigator.getUserMedia error: ", error);
    }

    $("#record").on('click', function () {
        document.getElementById("record").innerHTML = 'Recording...';
        $("#timer").show(0);

        navigator.mediaDevices
            .getUserMedia(constraints)
            .then(successCallback)
            .catch(errorCallback);
    });


    function stopWebCam() {
        if (video) {
            video.pause();
            video.src = '';
            video.load();
        }

        if (cameraStream && cameraStream.stop) {
            cameraStream.stop();
        }
        stream = null;
    }
} else {
    alert('getUserMedia support required to use this page');
}