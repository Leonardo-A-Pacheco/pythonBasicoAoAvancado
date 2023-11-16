import os
perguntas = [
    {
        'pergunta': 'How are you from?',
        'opcoes': ['a) como é o seu nome?', 'b) que horas são agora?', 'c) Poneis são azuis?', 'd) De onde você é?', 'e) Isso é uma bicicleta?'],
        'resposta': 'd) De onde você é?',
    },
    {
        'pergunta': 'What is your name?',
        'opcoes': ['a) Como você está?', 'b) Qual é o seu nome?', 'c) O que você está fazendo?', 'd) Quanto isso custa?', 'e7) que horas são agora?'],
        'resposta': 'b) Qual é o seu nome?'
    },
    {
         'pergunta': 'How old are you?',
        'opcoes': ['a) O que você quer?', 'b) Quantos anos você tem?', 'c) Você gosta de música?', 'd) Onde você mora?'],
        'resposta': 'b) Quantos anos você tem?'
    },
    {
        'pergunta': 'Where do you live?',
        'opcoes': ['a) Qual é a sua comida favorita?', 'b) Onde você trabalha?', 'c) O que você faz no seu tempo livre?', 'd) Onde você mora?'],
        'resposta': 'd) Onde você mora?'
    },
    {
        'pergunta': 'What time is it?',
        'opcoes': ['a) Você gosta de viajar?', 'b) Que horas são agora?', 'c) Como você foi para a escola?', 'd) O que você está vestindo?'],
        'resposta': 'b) Que horas são agora?'
    }, 
    {
        'pergunta': 'Can you speak English?',
        'opcoes': ['a) O que você fez ontem?', 'b) Você sabe tocar piano?', 'c) Você pode falar inglês?', 'd) Qual é o seu esporte favorito?'],
        'resposta': 'c) Você pode falar inglês?'
    },
    {
        'pergunta': "What's your favorite color?",
        'opcoes': ['a) Quem é o seu melhor amigo?', 'b) Qual é a sua cor favorita?', 'c) Como você vai para o trabalho?', 'd) O que você come no café da manhã?'],
        'resposta': 'b) Qual é a sua cor favorita?'
    },
    {
        'pergunta': 'Do you like to read books?',
        'opcoes': ['a) O que você está fazendo agora?', 'b) Você gosta de ler livros?', 'c) Qual é a sua sobremesa favorita?', 'd) Você tem irmãos?'],
        'resposta': 'b) Você gosta de ler livros?'
    },
    {
        'pergunta': 'Where did you go on your last vacation?',
        'opcoes': ['a) Como você aprendeu isso?', 'b) Onde você esteve nas suas últimas férias?', 'c) O que você tem na bolsa?', 'd) Você tem animais de estimação?'],
        'resposta': 'b) Onde você esteve nas suas últimas férias?'
    },
    {
        'pergunta': "What's the weather like today?",
        'opcoes': ['a) Como é o clima hoje?', 'b) O que você costuma fazer nos finais de semana?', 'c) Você gosta de nadar?', 'd) Qual é o seu prato preferido?'],
        'resposta': 'a) Como é o clima hoje?'
    },
    {
        'pergunta': 'Can you play the guitar?',
        'opcoes': ['a) Você toca guitarra?', 'b) O que você fará amanhã?', 'c) O que você assistiu na TV ontem?', 'd) Como você se sente hoje?'],
        'resposta': 'a) Você toca guitarra?'
    },
    {
        'pergunta': 'How do you get to work?',
        'opcoes': ['a) Você gosta de nadar?', 'b) Como você vai para o trabalho?', 'c) Qual é o seu filme favorito?', 'd) Você já viajou para o exterior?'],
        'resposta': 'b) Como você vai para o trabalho?'
    },
    {
        'pergunta': "What's your favorite food?",
        'opcoes': ['a) O que você fará no próximo feriado?', 'b) Qual é a sua comida favorita?', 'c) Você tem irmãs?', 'd) Você já correu uma maratona?'],
        'resposta': 'b) Qual é a sua comida favorita?'
    },
    {
        'pergunta': 'Why are you learning English?',
        'opcoes': ['a) Onde você estava ontem à noite?', 'b) Por que você está aprendendo inglês?', 'c) Você gosta de acampar?', 'd) Qual é o seu esporte favorito?'],
        'resposta': 'b) Por que você está aprendendo inglês?'
    },
    {
        'pergunta': 'Who is your best friend?',
        'opcoes': ['a) Quem é o seu melhor amigo?', 'b) O que você come no almoço?', 'c) Qual é a sua matéria favorita?', 'd) Você já visitou um museu?'],
        'resposta': 'a) Quem é o seu melhor amigo?'
    },
    {
        'pergunta': 'When is your birthday?',
        'opcoes': ['a) Quando é o seu aniversário?', 'b) O que você faz nas suas férias?', 'c) Você tem um animal de estimação?', 'd) Qual é o seu programa de TV favorito?'],
    }

]
# acessando primeiramente a lista que contem os dicionarios question
for question in perguntas:
    print(question['pergunta'])
    print()
# rodando loop para exbir as questões
    for op in question['opcoes']:
        print(op)
    print()
# rebebendo a resposta
    r = input('Qual letra da resposta correta? ')
# verificando certo ou errado

    if r == question['resposta'][0]:
        print('acertou')
    else:
        print('errou')    
    print('---------------------')
