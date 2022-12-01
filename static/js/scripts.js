$("form[name=signup_form").submit(function (e) {
  console.log("signup clicked")


  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/register",
    type: "POST",
    data: data,
    dataType: "json",
    success: function (resp) {
      console.log("successfully register new user")
      window.location.href = "/login";
    },
    error: function (resp) {
      console.log("error in signup")
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=login_form").submit(function (e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/auth",
    type: "POST",
    data: data,
    dataType: "json",
    success: function (resp) {
      window.location.href = "/dashboard";
    },
    error: function (resp) {
      console.log(resp)
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

// action of logoutbtn from newHome.html
$('#logoutbtn').click(function (e) {
  console.log("btn clicked")
  $.ajax({
    url: "/logout",
    type: "GET",
    success: function (resp) {
      window.location.href = "/";
    },
    error: function (resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=upload_form").submit(function (e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();
  console.log("upload form submission.")

  $.ajax({
    url: "/dashboard/upload/snippet",
    type: "POST",
    data: data,
    dataType: "json",
    success: function (resp) {
      console.log("successfully uploaded snippet")
      console.log(resp)
      window.location.href = "/dashboard/upload";
    },
    error: function (resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});


// function copyFunction() {
//   const copyText = document.getElementById("code").textContent;
//   const textArea = document.createElement('textarea');
//   textArea.textContent = copyText;
//   document.body.append(textArea);
//   textArea.select();
//   document.execCommand("copy");
// }

// document.getElementById('copy').addEventListener('click', copyFunction);

jQuery(document).ready(function ($) {
  var copyid = 0;
  $('pre').each(function () {
    copyid++;
    $(this).attr('data-copyid', copyid).wrap('<div class="pre-wrapper"/>');
    $(this).parent().css('margin', $(this).css('margin'));
    $('<button class="copy-snippet">Copy</button>').insertAfter($(this)).data('copytarget', copyid);
  });

  $('body').on('click', '.copy-snippet', function (ev) {
    ev.preventDefault();

    var $copyButton = $(this);

    $pre = $(document).find('pre[data-copyid=' + $copyButton.data('copytarget') + ']');
    if ($pre.length) {
      var textArea = document.createElement("textarea");

      // Place in top-left corner of screen regardless of scroll position.
      textArea.style.position = 'fixed';
      textArea.style.top = 0;
      textArea.style.left = 0;

      // Ensure it has a small width and height. Setting to 1px / 1em
      // doesn't work as this gives a negative w/h on some browsers.
      textArea.style.width = '2em';
      textArea.style.height = '2em';

      // We don't need padding, reducing the size if it does flash render.
      textArea.style.padding = 0;

      // Clean up any borders.
      textArea.style.border = 'none';
      textArea.style.outline = 'none';
      textArea.style.boxShadow = 'none';

      // Avoid flash of white box if rendered for any reason.
      textArea.style.background = 'transparent';

      //Set value to text to be copied
      textArea.value = $pre.text();

      document.body.appendChild(textArea);
      textArea.select();

      try {
        document.execCommand('copy');
        $copyButton.text('Copied').prop('disabled', true);;
      } catch (err) {
        $copyButton.text('FAILED: Could not copy').prop('disabled', true);;
      }
      setTimeout(function () {
        $copyButton.text('Copy').prop('disabled', false);;
      }, 3000);
      textArea.remove();
      //   const copyText = document.getElementById("code").textContent;
      //   const textArea = document.createElement('textarea');
      //   textArea.textContent = copyText;
      //   document.body.append(textArea);
      //   textArea.select();
      //   document.execCommand("copy");
      // }

      // document.getElementById('copy').addEventListener('click', copyFunction);
    }
  });
});