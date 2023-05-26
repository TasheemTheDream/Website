
document.addEventListener("DOMContentLoaded", function(){
    var element = document.getElementById("myTooltip");
    var tooltip = new bootstrap.Tooltip(element, {
        title: "<div class='card' triggers='hover>\
        <div class='card-body'>\
          <h5 class='card-title'>Special title treatment</h5>\
          <p class='card-text'>With supporting text below as a natural lead-in to additional content.</p>\
          <a href='#' class='btn btn-primary'>Go somewhere</a>\
        </div>\
      </div>",
        html: true
    });
});
