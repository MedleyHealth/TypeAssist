// Fifty-two year old woman with metastatic breast cancer. Reassess cardiac function after adriamycin-based chemotherapy.
// Reason for Exam: MRI of the brain with and without gadolinium. There is no evidence of intracranial hemorrhage or mass lesion.

$(document).ready(function () {
    $("#type-box").on("input", function (event) {

        var box = document.getElementById("type-box");
        var contents = box.innerText;

        contents = contents.replace(/(\r\n|\n|\r)/gm, "");
        console.log("'" + contents + "'")

        if (contents.endsWith("Fifty-tw")) {
            box.innerHTML += '<span class="suggestion">o year old woman<span>';
            setCursor(8);

            setTimeout(function (){
                box.innerText = 'Fifty-two year old woman'
                setCursor(24);
            }, 1000);
        }

        if (contents.endsWith("meta")) {
            box.innerHTML = box.innerHTML.replace('<br>', '');
            box.innerHTML += '<span class="suggestion">static breast cancer<span>';
            setCursor(34);

            setTimeout(function (){
                box.innerText = 'Fifty-two year old woman with metastatic breast cancer'
                setCursor(54);
            }, 1000);
        }

        if (contents.endsWith("car")) {
            box.innerHTML = box.innerHTML.replace('<br>', '');
            box.innerHTML += '<span class="suggestion">diac function<span>';
            setCursor(68);

            setTimeout(function (){
                box.innerText = 'Fifty-two year old woman with metastatic breast cancer. Reassess cardiac function'
                setCursor(81);
            }, 1000);
        }

        if (contents.endsWith("adr")) {
            box.innerHTML = box.innerHTML.replace('<br>', '');
            box.innerHTML += '<span class="suggestion">iamycin-based chemotherapy<span>';
            setCursor(91);

            setTimeout(function (){
                box.innerText = 'Fifty-two year old woman with metastatic breast cancer. Reassess cardiac function after adriamycin-based chemotherapy'
                setCursor(117);
            }, 1000);
        }
    });
});

function setCursor(pos) {
    var tag = document.getElementById("type-box");

    // Creates range object
    var setpos = document.createRange();

    // Creates object for selection
    var set = window.getSelection();

    // Set start position of range
    setpos.setStart(tag.childNodes[0], pos);

    // Collapse range within its boundary points
    // Returns boolean
    setpos.collapse(true);

    // Remove all ranges set
    set.removeAllRanges();

    // Add range with respect to range object.
    set.addRange(setpos);

    // Set cursor on focus
    tag.focus();
}


(function ($) {
    "use strict";


    /*==================================================================
    [ Focus Contact2 ]*/
    $('.input2').each(function(){
        $(this).on('blur', function(){
            if($(this).val().trim() != "") {
                $(this).addClass('has-val');
            }
            else {
                $(this).removeClass('has-val');
            }
        })    
    })
            
  
    
    /*==================================================================
    [ Validate ]*/
    var name = $('.validate-input input[name="name"]');
    var email = $('.validate-input input[name="email"]');
    var message = $('.validate-input textarea[name="message"]');


    $('.validate-form').on('submit',function(){
        var check = true;

        if($(name).val().trim() == ''){
            showValidate(name);
            check=false;
        }


        if($(email).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
            showValidate(email);
            check=false;
        }

        if($(message).val().trim() == ''){
            showValidate(message);
            check=false;
        }

        return check;
    });


    $('.validate-form .input2').each(function(){
        $(this).focus(function(){
           hideValidate(this);
       });
    });

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    

})(jQuery);