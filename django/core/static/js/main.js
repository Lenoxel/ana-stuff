$(document).ready(function(){
    $(".evaluation-button").each(function(){
        if (this.dataset && this.dataset.rated) {
            let alreadyRated = localStorage.getItem(this.dataset.rated);
            if (alreadyRated) {
                $(this).prop('disabled', true);
                $(this).text("Já avaliado");
            }
        }
    });
});

$(function() {
    $("#redirectToHome").click(function() {
        $("homeId").addClass("active");
        localStorage.setItem("lastTab", $("homeId").attr("id"));
    });

    let last = localStorage.getItem("lastTab");
    if (last) {
        $("#" + last).click();
    }
});

$(function() {
    $("#tabsList > li").click(function() {
        $(this).siblings().removeClass("active");
        $(this).addClass("active");
        localStorage.setItem("lastTab", $(this).attr("id"));
    });

    let last = localStorage.getItem("lastTab");
    if (last) {
        $("#" + last).click();
    }
});

$(function() {
    $("#categoryList > a").click(function() {
        $(this).siblings().removeClass("active");
        $(this).addClass("active");
        showFilteredCategories(this.id);
    });
});


function showFilteredCategories(category) {
    $("#productsArea > div").each(function() {
        let product = this;
        if (product && product.dataset && product.dataset.category) {
            if (product.dataset.category === category) {
                $(this).slideDown();
                product.style.display = "block";
            } else {
                $(this).slideUp();
                product.style.display = "none";
            }
        }
    });
}

function showEvaluationModal(pk, name) {
    if (pk && name) {
        let buttonSubmitEvaluation = $("#submit_evaluation");
        buttonSubmitEvaluation[0].dataset.productId = pk;

        $('#evaluatorName').val("");
        $('#evaluatorEmail').val("");
        $('#evaluatorComment').val("");
        $('#evaluatorEvaluation > input').each(function() {
            $(this).prop('checked', false);
        });
        $('#evaluationModalTitle').text("Avaliação do Produto - " + name);
        $('#evaluationModalFooter').html('');
        $('#evaluationModal').modal();
    }
}

$(function() {
    $("#submit_evaluation").click(function() {
        let formattedEvaluation;
        let productId = $('#submit_evaluation').data('productId');
        $('#evaluatorEvaluation > input').each(function() {
            if ($(this).is(':checked')) {
                formattedEvaluation = $(this).val();
                return;
            }
        });
        $.ajax({
            type: "POST",
            url: '/produto/avaliar/',
            data: {
                evaluator_name: $('#evaluatorName').val(),
				evaluator_email: $('#evaluatorEmail').val(),
                evaluator_comment: $('#evaluatorComment').val(),
                evaluator_evaluation: formattedEvaluation,
                product_id: productId,
				csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(data){
                $('#evaluationModalAlert').html('<span class="alert alert-success" role="alert">Sua avaliação foi salva com sucesso!</span>');
                let currentEvaluatedProductButton = "[data-rated='alreadyRated_" + productId + "']";
                localStorage.setItem("alreadyRated_" + productId, true);
                $(currentEvaluatedProductButton).prop('disabled', true);
                $(currentEvaluatedProductButton).text("Já avaliado");
                setTimeout(function(){
                    $('#evaluationModal').modal('hide');
                }, 2000);
            },
            error: function(){
                $('#evaluationModalAlert').html('<span class="alert alert-danger alert-dismissible fade show" role="alert">Ocorreu um erro ao salvar sua avaliação.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></span>');
            }
        });
    });
});

