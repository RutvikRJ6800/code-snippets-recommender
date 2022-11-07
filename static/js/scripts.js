$("form[name=signup_form").submit(function(e) {
    console.log("signup clicked")
    
  
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();
  
    $.ajax({
      url: "/register",
      type: "POST",
      data: data,
      dataType: "json",
      success: function(resp) {
        console.log("successfully register new user")
        window.location.href = "/login";
      },
      error: function(resp) {
        console.log("error in signup")
        $error.text(resp.responseJSON.error).removeClass("error--hidden");
      }
    });
  
    e.preventDefault();
  });
  
  $("form[name=login_form").submit(function(e) {
  
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();
  
    $.ajax({
      url: "/auth",
      type: "POST",
      data: data,
      dataType: "json",
      success: function(resp) {
        window.location.href = "/dashboard";
      },
      error: function(resp) {
        console.log(resp)
        $error.text(resp.responseJSON.error).removeClass("error--hidden");
      }
    });
  
    e.preventDefault();
  });
  
  // action of logoutbtn from newHome.html
  $('#logoutbtn').click(function(e){ 
    console.log("btn clicked")
    $.ajax({
      url: "/logout",
      type: "GET",
      success: function(resp) {
        window.location.href = "/";
      },
      error: function(resp) {
        $error.text(resp.responseJSON.error).removeClass("error--hidden");
      }
    });
  
    e.preventDefault();
  });
  
  $("form[name=upload_form").submit(function(e) {
  
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();
    console.log("upload form submission.")
  
    $.ajax({
      url: "/dashboard/upload/snippet",
      type: "POST",
      data: data,
      dataType: "json",
      success: function(resp) {
        console.log("successfully uploaded snippet")
        console.log(resp)
        window.location.href = "/dashboard/upload";
      },
      error: function(resp) {
        $error.text(resp.responseJSON.error).removeClass("error--hidden");
      }
    });
  
    e.preventDefault();
  });