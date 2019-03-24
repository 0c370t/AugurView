var initialImage = "";



function uploadFile(){
  // jQuery doesn't really help me with file inputs, so I have to do it with DOM selector
  fileInput = document.getElementById("pictureUploadInput");
  imageDisplay = $("#userImage");
  if(fileInput.value){
    file = fileInput.files[0];
    // File is now available for the upload
    formData = new FormData();
    formData.append('file', file);
    $.ajax({
      url:"uploadImage",
      type:"post",
      data:formData,
      contentType: false,
      processData: false,
      success:uploadFileCallback
    });
  } else {
    alert("Please select an image to use");
  }
}
function uploadFileCallback(data,status){
  initialImage = data;
  $("#userImage").attr('src',initialImage);
}
function modifyImage(){
  endpointInput = $("#endpointSelector");
  imageDisplay = $("#userImage");
  if(!endpointInput.val()){
    alert("Please select an operation to use");
  } else if (initialImage === ""){
    alert("Please upload an image first");
  }

}
