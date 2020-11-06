$(function () {
    /* Functions */
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal .modal-content").html("");
                $("#modal").modal('show');
            },
            success: function (data) {
                $("#modal .modal-content").html(data.html_form);
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
                if (data.form_is_valid ) {
                    $("#project_table tbody").html(data.html_project_list);
                    $("#modal").modal("hide");
                } else {
                    $("#modal .modal-content").html(data.html_form);
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
    $("#project_table").on("click", ".js-update-project", loadForm);
    $("#modal").on("submit", ".js-project-update-form", saveForm);

    // Delete book
    $("#project_table").on("click", ".js-update-project", loadForm);
    $("#modal").on("submit", ".js-project-delet", saveForm);

});