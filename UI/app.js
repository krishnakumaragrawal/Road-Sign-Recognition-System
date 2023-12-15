Dropzone.autoDiscover = false;

function init() {
    let dz = new Dropzone("#dropzone", {
        url: "/",
        maxFiles: 1,
        addRemoveLinks: true,
        dictDefaultMessage: "Some Message",
        autoProcessQueue: false
    });


    dz.on("addedfile", function() {
        if (dz.files[1] != null) {
            dz.removeFile(dz.files[0]);
        }
    });

    dz.on("complete", function (file) {
        let imageData = file.dataURL;

        var url = "http://127.0.0.1:5000/classify_images"


        $.post(url, {
            image_data: file.dataURL
        }, 
        function(data, status) {
            console.log(data);
            if (!data || data.length==0) {
                $("#error").show();
                $("#resultHolder").hide();
            }

            let match = data[data.length-1]
            if (match) {
                $("#error").hide();
                $("#resultHolder").show();
                $("#resultHolder").html(match.class)
            }
        });

    });

    $("#submitBtn").on('click', function (e) {
        dz.processQueue();
    });
}

function displayImage(){
    var selectBox = document.getElementById("sign-select")
    var selectedValue = selectBox.options[selectBox.selectedIndex].value;
    var imageElement = document.getElementById("display-image")

    if (selectedValue !== ""){
        imageElement.src = selectedValue
    }
    else{
        imageElement.src = "";
    }
}


$(document).ready(function() {
    console.log( "ready!" );
    $("#error").hide();
    $("#resultHolder").hide();

    init();
});