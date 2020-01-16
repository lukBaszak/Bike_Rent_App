 function parseMillisecondsIntoTime(milliseconds){
                          //Get hours from milliseconds
                          var hours = milliseconds / (1000*60*60);
                          var absoluteHours = Math.floor(hours);
                          var h = absoluteHours > 9 ? absoluteHours : '0' + absoluteHours;

                          //Get remainder from hours and convert to minutes
                          var minutes = (hours - absoluteHours) * 60;
                          var absoluteMinutes = Math.floor(minutes);
                          var m = absoluteMinutes > 9 ? absoluteMinutes : '0' +  absoluteMinutes;

                          //Get remainder from minutes and convert to seconds
                          var seconds = (minutes - absoluteMinutes) * 60;
                          var absoluteSeconds = Math.floor(seconds);
                          var s = absoluteSeconds > 9 ? absoluteSeconds : '0' + absoluteSeconds;

                          return h + ':' + m + ':' + s;
                          }

function getTrTag(object) {

    var tr = document.createElement('tr');




    var start_date = new Date(object.start);
    var end_date = new Date(object.end)



    start_date_formatted = start_date.getDay() + "." + appendLeadingZeroes(start_date.getMonth()+1) + "." + start_date.getFullYear() + ' ' + start_date.getHours() + '.' + start_date.getMinutes() + '.' + start_date.getSeconds();
    end_date_formatted = end_date.getDay() + "." + appendLeadingZeroes(end_date.getMonth()+1) + "." + end_date.getFullYear() + ' ' + end_date.getHours() + '.' + end_date.getMinutes() + '.' + end_date.getSeconds();



    duration = end_date - start_date;
    duration_formatted = parseMillisecondsIntoTime(duration);



    if(object.price != null) {
        tr.innerHTML = '<td>' + '<i class="fas fa-info-circle"></i>' +  '</td>' +
                    '<td>' + start_date_formatted + '</td>' +

                    '<td>' + end_date_formatted + '</td>' +
                    '<td>' + duration_formatted + '</td>' +
                    '<td>' + object.price + "zl" + '</td>';
    }

    else {
        tr.innerHTML = '<td>' + 'lol' +  '</td>' +
         '<td>' + start_date_formatted + '</td>' +
          '<td>' + " - " + '</td>' +
          '<td>' + " - " + '</td>' +
          '<td>' + " - " + '</td>';

    }

    tr.onclick = function(evt) {
        popupWindow = window.open(
            'details/'+object.id,'popUpWindow','height=500 ,width=500,left=10,top=10,' +
            'scrollbars=no,toolbar=no,menubar=no,location=no,' +
            'directories=no,status=yes' +
            'details={{object}}')
    };






    return tr;
}


function appendLeadingZeroes(n){
      if(n <= 9){
        return "0" + n;
      }
      return n
        }

