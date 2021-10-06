$(document).ready(function() {
    $('.evaluation-button').each(() => {
        if (this.dataset && this.dataset.rated) {
            const alreadyRated = localStorage.getItem(this.dataset.rated);
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

    const last = localStorage.getItem("lastTab");
    if (last) {
        $(`#${last}`).click();
    }
});

$(function() {
    $('#tabsList > li').click(function() {
        $(this).siblings().removeClass("active");
        $(this).addClass("active");
        localStorage.setItem("lastTab", $(this).attr("id"));
    });

    const last = localStorage.getItem("lastTab");
    if (last) {
        $(`#${last}`).click();
    }
});

$(function() {
    $('#categoryList > a').click(function() {
        $(this).siblings().removeClass("active");
        $(this).addClass("active");
        showFilteredCategories(this.id);
    });
});


showFilteredCategories = (category) => {
    $("#productsArea > div").each(() => {
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

showEvaluationModal = (pk, name) => {
    if (pk && name) {
        let buttonSubmitEvaluation = $('#submit_evaluation');
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
        const productId = $('#submit_evaluation').data('productId');
        $('#evaluatorEvaluation > input').each(() => {
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
            success: function(data) {
                $('#evaluationModalAlert').html('<span class="alert alert-success" role="alert">Sua avaliação foi salva com sucesso!</span>');
                const currentEvaluatedProductButton = `[data-rated='alreadyRated_${productId}']`;
                localStorage.setItem(`alreadyRated_${productId}`, true);
                $(currentEvaluatedProductButton).prop('disabled', true);
                $(currentEvaluatedProductButton).text("Já avaliado");
                setTimeout(() => {
                    $('#evaluationModal').modal('hide');
                }, 2000);
            },
            error: function() {
                $('#evaluationModalAlert').html('<span class="alert alert-danger alert-dismissible fade show" role="alert">Ocorreu um erro ao salvar sua avaliação.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></span>');
            }
        });
    });
});

$(function() {
    $("#submit_message").click(() => {
        const name = $('#sentByName').val();
        const email = $('#sentByEmail').val();
        const subject = $('#messageSubject').val();
        const comment = $('#messageComment').val();
        const csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();

        if (name && email && validateEmail(email) && subject && comment) {
            $.ajax({
                type: 'POST',
                url: '/contato/mensagem/enviar/',
                data: {
                    name,
                    email,
                    subject,
                    comment,
                    csrfmiddlewaretoken,
                },
                success: function() {
                    document.getElementById('sendMessageForm').reset();
                    $('#sendMessageSuccess').html('<span class="alert alert-success alert-dismissible fade show" role="alert">Mensagem enviada com sucesso!<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></span>');
                },
                error: function() {}
            });
        }
    });
});

function validateEmail(email) {
    const res = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return res.test(String(email).toLowerCase());
}