var Script = function () {

    $().ready(function() {
        // validate the comment form when it is submitted
        $("#feedback_form").validate();

        // Validação de Formulários de Registro de Usuário
        $("#usuario_form").validate({
            rules: {
                nome: {
                    required: true,
		    minlength: 2
                },
		sobrenome: {
                    required: true,
    		    minlength: 2
                },
                endereco: {
                    required: true,
                },
                senha: {
                    required: true,
                    minlength: 5
                },
                confirmar_senha: {
                    required: true,
                    minlength: 5,
                    equalTo: "#senha"
                },
                email: {
                    required: true,
                    email: true
                },                
                agree: "required"
            },
            messages: {                
                nome: {
                    required: "Por favor, digite o nome do usuário.",
                    minlength: "O nome do usuário deve ser pelo menos 2 caracteres."
                },
		sobrenome: {
                    required: "Por favor, digite o sobrenome do usuário.",
                    minlength: "O sobrenome do usuário deve ser pelo menos 2 caracteres."
                },
                endereco: {
                    required: "Por favor, digite o endereço.",
                },
                senha: {
                    required: "Por favor, digite a sua senha.",
                    minlength: "Sua senha precisa ter pelo menos 5 caracteres."
                },
                confirm_password: {
                    required: "Por favor, confirme sua senha.",
                    minlength: "Sua senha precisa ter pelo menos 5 caracteres.",
                    equalTo: "Por favor, digite a mesma senha informada anteriormente."
                },
                email: "Por favor, digite um endereço de email válido.",
                agree: "Queira aceitar os nossos termos e condições."
            }
        });

        // propose username by combining first- and lastname
        $("#username").focus(function() {
            var firstname = $("#firstname").val();
            var lastname = $("#lastname").val();
            if(firstname && lastname && !this.value) {
                this.value = firstname + "." + lastname;
            }
        });

        //code to hide topic selection, disable for demo
        var newsletter = $("#newsletter");
        // newsletter topics are optional, hide at first
        var inital = newsletter.is(":checked");
        var topics = $("#newsletter_topics")[inital ? "removeClass" : "addClass"]("gray");
        var topicInputs = topics.find("input").attr("disabled", !inital);
        // show when newsletter is checked
        newsletter.click(function() {
            topics[this.checked ? "removeClass" : "addClass"]("gray");
            topicInputs.attr("disabled", !this.checked);
        });
    });


}();
