$(function () {
    /* Functions */
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-project .modal-content").html("");
                $("#modal-project").modal('show');
            },
            success: function (data) {
                $("#modal-project .modal-content").html(data.html_form);
            }
        });
    };
    var saveForm = function () {

        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#modal-project .modal-content").html(data.html_book_list);
                    $("#modal-project").modal("hide");
                } else {
                    $("#modal-book .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */

    // Create book
    // $(".js-create-book").click(loadForm);
    // $("#modal-book").on("submit", ".js-book-create-form", saveForm);
    //
    // // Update book
    // $("#book-table").on("click", ".js-update-book", loadForm);
    // $("#modal-book").on("submit", ".js-book-update-form", saveForm);

    // Delete book
    $("#project-table").on("click", ".js-delete-project", loadForm);
    $("#project-table").on("submit", ".js-project-delet", saveForm);

});

function go_delet() {
    alert("dddd")
    // var id = name
    // if (name === "") {
    //   window.location = '';
    // }
    // else {
    //   var url = "/delet/" + id
    //   window.location = url;
    // }
    // window.location = "/"
    // 跳至網址
}