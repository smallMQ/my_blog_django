   fileInput.bind("change", function() {
          var fileName = fileInput.val();
          var isImage = new RegExp("(\\.(" + settings.imageFormats.join("|") + "))$", "i"); // /(\.(webp|jpg|jpeg|gif|bmp|png))$/

          if (fileName === "") {
            alert(imageLang.uploadFileEmpty);

            return false;
          }

          if (!isImage.test(fileName)) {
            alert(imageLang.formatNotAllowed + settings.imageFormats.join(", "));

            return false;
          }
          loading(true);
          var submitHandler = function() {
            var uploadIframe = document.getElementById(iframeName);
            uploadIframe.onload = function() {
              loading(false);
              var formData = new FormData();
              //获取需要上传的文件，追加到formData中以json的方式提交
              formData.append("file", $("#file")[0].files[0]);
              var action = settings.imageUploadURL + (settings.imageUploadURL.indexOf("?") >= 0 ? "&" :
                "?") + "guid=" + guid;
              $.ajax({
                type: "post",
                url: action,
                data: formData,
                dataType: "json",
                async: false,
                processData: false,
                contentType: false,
                success: function(data) {
                //data返回来的数据
                  if (data.success == 1) {
           			//回显的url
                    dialog.find("[data-url]").val(data.data.url);
                  } else {
                    alert(data.msg)
                  }
                },
              });
              return false;
            };
          };

          dialog.find("[type=\"submit\"]").bind("click", submitHandler).trigger("click");
        });
