<Instruções Gerais>

Vamos fazer um bot que ficara entrando no site "https://www.exteriores.gob.es/Embajadas/brasilia/pt/Embajada/Paginas/Cita-previa.aspx" e verifica se há agendamentos disponíveis.

Ao fazer uma requisição, a primeira coisa que aparece no site é um alert box do javascript dizendo bem vindo e pedindo pra clicar no botão "Ok" para continuar.

Ao clicar em "Ok" no alert box, uma página é carregada e exibe a seguinte mensagem: "To request an appointment, click on the continue button
Para solicitar cita pulse en el botón continuar"

Logo abaixo essa mensagem, tem um botão verde escrito "Continue / Continuar" que ao clicar nele, abre uma nova página com informações.

Nessa nova página, preciso avaliar se há agendamentos disponíveis. Quando não há agendamentos disponíveis, preciso que o bot retorne "Não há agendamentos disponíveis".

Quando há agendamentos disponíveis, preciso que o bot retorne "Há agendamentos disponíveis".

Para saber se há ou não agendamentos disponíveis, basta verifica o texto que essa página possui. Quando não há agendamentos disponíveis, o texto exibido é o seguinte:

"EMBAJADA DE ESPAÑA EN BRASILIA
No hay horas disponibles.
Inténtelo de nuevo dentro de unos días."

</Instruções Gerais>
