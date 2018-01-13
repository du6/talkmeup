/* global MediaRecorder $ */
/*eslint no-console: 0*/

const record = document.getElementById('record')
const stop = document.getElementById('stop')
const csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
$("#record").hide(0);
$("#timer").hide(0);

if (!navigator.mediaDevices){
  alert('getUserMedia support required to use this page')
}

const chunks = []
let onDataAvailable = (e) => {
  chunks.push(e.data)
}

// Not showing vendor prefixes.
navigator.mediaDevices.getUserMedia({
  audio: true,
  video: {
    width: { ideal: 480 },
    height: { ideal: 360 }
  }
}).then((mediaStream) => {
  const recorder = new MediaRecorder(mediaStream)
  recorder.ondataavailable = onDataAvailable
  const video = document.querySelector('video')
  const url = window.URL.createObjectURL(mediaStream)
  video.src = url
  $("#record").show(0);
  $("#record").click(() => {
    $(this).unbind("click");
    document.getElementById("record").innerHTML = 'Recording...';
    $("#timer").show(0);
    recorder.start();
    var count = 30;
    var counter = setInterval(() => {
      count = count - 1;
      document.getElementById("timer").innerHTML = count; // watch for spelling
      if (count <= 0) {
        recorder.stop();
        clearInterval(counter);
      }
    }, 1000);
  });

  recorder.onstop = (e) => {
    console.log('e', e)
    console.log('chunks', chunks)
    document.getElementById("record").innerHTML = 'Uploading...';
    const bigVideoBlob = new Blob(chunks, { 'type' : 'video/webm; codecs=webm' })
    const filename = csrftoken + '.webm';
    const file = new File([bigVideoBlob], filename);
    let fd = new FormData()
    fd.append('description', filename)
    fd.append('document', file)
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });
    $.ajax({
      type: 'POST',
      url: '/uploads/',
      data: fd,
      processData: false,
      contentType: false
    }).done(function(data) {
      console.log(data)
      location.href = 'check';
    })
  }
}).catch(function(err){
  console.log('error', err)
})

