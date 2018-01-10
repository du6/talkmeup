setTimeout(function () {
		  
		  $('.loader-wrap').fadeOut();
			  
		
}, 1200);


var count=30;


function timer()
{
  count=count-1;
  if (count < 0)
  {
     clearInterval(counter);
     return;
  }

 document.getElementById("timer").innerHTML=count; // watch for spelling
}


