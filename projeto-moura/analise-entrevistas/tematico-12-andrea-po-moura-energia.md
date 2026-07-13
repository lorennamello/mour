# Análise Temática — Andrea (PO / Product Owner Moura Energia)

**Contexto:** duas conversas — uma reunião de planejamento/mapeamento de stakeholders (mais tática) e uma imersão longa sobre histórico, modelo de negócio e contrato Vivo. Andrea é a orquestradora entre fábrica, engenharia, comercial e financeiro para o produto Energia como Serviço.

---

## 1. Proposta de valor — o que entrega e para quem

**Fato — elevator pitch dela, quando pedido diretamente:** "O serviço da energia como serviço, a gente presta um serviço de backup contínuo, de backup de energia contínuo [...] a gente não deixa a tua disponibilidade de serviço parar. Com isso [...] a gente mantém seus SLA necessários, a gente cumpre regras regulamentares e a gente te proporciona zero CAPEX de investimento [...] a redução de OIM [...] apenas a prestação de serviços da gente, e o foco no core business."
**Fato — autocrítica imediata sobre esse próprio pitch:** "Isso pode não estar ideal. Essa é a crítica que a gente sempre faz dentro de casa. Será que é isso mesmo que a telefônica tem que ouvir? Será que a gente está acertando?"
**Fato — reformulação posterior, mais específica sobre o que falta comunicar:** "para Telecom [...] a gente está enxergando uma parcela da operadora, que é a parcela de campo, mas a gente não está olhando a parcela de que isso dá no resultado, a gente não está trazendo isso à tona. Acho que a gente está falando de menos."
**Fato — analogia usada para explicar o valor de "continuidade" da energia:** "Se eu sou cliente da Vivo [...] se falta energia, eu vou ter um problema. Então, quem está me garantindo energia? A Moura. Então, se a Moura está bem, meu cliente também está bem."

**Interpretação:** Andrea é quem mais reconhece explicitamente que o discurso de valor atual está incompleto — ela não apenas descreve o pitch, mas audita sua própria eficácia em tempo real durante a entrevista, sugerindo autoconsciência institucional do problema (mesmo sem tê-lo resolvido).

---

## 2. Desafios internos por área

### Produto (a área dela, PO)
**Fato — Telecom ainda não é um "produto de prateleira" como o BES:** "Quando a gente vai para a telecom, é algo totalmente não padronizável [...] o produto do Telecom, às vezes, não é uma coisa só, porque a telefônica tem um padrão, a TIM tem outro padrão [...] tem muita customização que o comercial [...] ainda não assumiu."
**Fato — problema de conectividade/OPEX gerado por decisão técnica não calibrada:** "a gente começou com o chip da Claro, aí depois disse, não, a gente tem que ir para a multi-operadora [...] teve o estouro de dados, porque o IoT não estava calibrado [...] estava dando cinco mil reais" (quando esperavam ~mil).
**Fato — falha de geração de ticket automático:** "às vezes, acontece do site ser furtado e não gerar um ticket [...] na plataforma da gente. Então, isso é um problema também que está tendo."

### Comercial (via a lente da PO)
**Fato — dúvida sobre estar falando com os stakeholders certos:** "será que a gente está acertando, a gente está falando com a pessoa correta mesmo. Quem é que define isso? Quem vem de cima ou quem vem de baixo?"
**Fato — percepção de resistência da operação do cliente:** "quem está na operação vai dizer assim, se eu botar esses caras aí, eu vou perder meu emprego [...] E o cara de cima, ele diz assim, opa, isso aqui eu vou ter uma otimização."

### Financeiro (limites da modelagem)
**Fato — cap de furto do contrato Telefônica já sendo superado na prática:** "o nosso [índice de furto] já está em torno de 6%[.] Mas hoje, no contrato [...] anualmente, cada site tem direito a R$1.350 de furto [...] esse valor já está acima [do previsto]."
**Fato — dificuldade real de custo de instalação em rooftop:** "a cada 15 andares, o valor do guincho, do guindaste, vai aumentando meio que exponencialmente [...] Para modelar [...] é meio que impossível."

### Operação
**Fato — problema de conectividade em campo:** chip dedicado a uma operadora causando falha fora da área de cobertura; falta de etiquetagem/ticket automática em furtos; cadeado Bluetooth insuficiente para impedir arrombamento com marreta.

---

## 3. Áreas internas — como ela percebe outras áreas (reunião de planejamento é rica nesse ponto)

**Fato — Daniel (financeiro):** "toda a parte de negócios, de contrato, de pagamento, de faturamento [...] Quando é para novos negócios [...] aí esses novos negócios, a área de PO se envolve para modelar [...] o Daniel é como se fosse também um validador dessa modelagem [...] ele não tem a responsabilidade na modelagem dos novos negócios."
**Fato — José Espinosa:** "a operação do contrato, a execução [...] Ele já trabalhou bastante [...] mais de 10 anos, na TIM, nessa parte de infraestrutura [...] Ele vai dizer, ah, tem pontos de melhoria aqui, acolá."
**Fato — Josiele:** "faz a gestão do contrato [...] atendimento ao cliente [...] o cliente é Moro Energia [...] Josiele faz um exemplo de requisitos, alinha os requisitos com a fábrica, alinha os requisitos com a engenharia, faz tudo de dentro de casa." Esclarece que Josiele está no DCBE (dentro da fábrica/ACMO), não na Moura Energia, e seu papel é "mais de interface [...] mais de marketing do que de engenharia."
**Fato — Spartacus (ex-diretor do ITEM):** "ele é meio que o CTO da gente [...] tudo que é técnico passa por ele [...] ele definiu junto com o Marcos Malveira a solução técnica [...] vocês podem explorar tudo [...] Porque ele desenhou junto com o Thiago Melo a solução."
**Fato — Francisco (TI):** "a visão dele é mais estrutural de plataforma [...] ele pode trazer [...] se a gente um dia vai querer vender essa plataforma para a operadora, ou se ela já tem isso."
**Fato — Thiago Mello:** "ele é o comercial [...] ele que foi atrás dessa [...] esse negócio. Ele que se juntou com o Gustavo [...] tem contato das pessoas [...] a pessoa que vocês precisam mais explorar [...] ele nunca vai ser só um respondedor de perguntas [...] vai sempre estimular, sempre vai gerar [...] reflexões."
**Fato — Gustavo:** "olha para frente [...] pode trazer lições aprendidas [...] é perguntar para ele qual o objetivo, qual a expectativa dele pelo projeto [...] uma dor dele, que eu sei, é furto."

**Interpretação:** o mapeamento de Andrea revela uma estrutura de governança altamente pessoal/informal — cada área tem um "dono" claro, mas a integração entre eles (ex.: TI ↔ ITEM ↔ Operação ↔ Comercial) depende fortemente de quem "costura" manualmente essas pontas, e ela mesma se posiciona como essa costureira central, o que é consistente com relatos de outros entrevistados sobre gargalos de coordenação.

---

## 4. Modelo comercial — como a venda acontece na prática

**Fato — origem do negócio:** ideia trazida por **Thiago Mello**, oportunidade percebida primeiro na **TIM** (não Telefônica); trial de 20 sites reais (Greenfield e rooftop), sem cobrança de aluguel — "compra ao final se der certo."
**Fato — resultado do trial TIM:** durante os 3 meses, houve um furto e "não se teve nenhum chamado para telefone, para a TIM. Todos esses chamados [...] foram todos para Moro" — usado como prova de conceito; ainda assim, a **TIM comprou o ativo, não contratou o serviço**.
**Fato — por que TIM comprou e não alugou (hipótese dela, a confirmar com Thiago Mello):** questão de CAPEX/EBITDA — TIM não enxergava o benefício contábil do IFRS16 que a Telefônica viu; também menciona confusão institucional na TIM sobre quem detém o CAPEX de infraestrutura.
**Fato — como a Telefônica entrou:** Thiago Mello teria usado o resultado do trial TIM como argumento comercial junto à Telefônica; a Telefônica abriu um edital (a Moura ajudou a construí-lo), inicialmente focado no gabinete T2.
**Fato — negociação do contrato girou fortemente em torno de quem assume o risco de furto:** inicialmente a Telefônica queria 100% de responsabilidade da Moura; negociação levou quase 1 ano até chegar a um cap contratual — "Isso foi um ganho, isso foi um sonho, porque foi tanta briga."

---

## 5. Visão sobre os clientes

**Fato — Telefônica hoje:** relação "muito colaborativa"; elogios de tempo de resposta e prontidão (repetido por outros); Espinosa (que veio da TIM) teria conversado recentemente com o responsável da Telefônica sobre o contrato e recebido feedback positivo.
**Fato — arquétipo TIM (via o caso do trial):** interessada em inovação, mas travada por questões contábeis/institucionais internas na hora de decidir entre compra e aluguel.
**Fato — segmentação Greenfield x rooftop, com implicação direta na exposição a furto:** hoje ~90% Greenfield / ~10% rooftop — inverso da modelagem original (85%/15%), o que significa mais exposição ao risco de furto do que planejado.
**Fato — clientes pequenos não são excluídos:** participaram de um BID da Algar com apenas 75 sites — "a gente não deixou de oferecer [...] a gente está no momento de entender."

---

## 6. Barreiras de expansão

**Fato — dúvida sobre estar falando com as pessoas certas** (repetida, ver seção 2).
**Fato — medo de perda de protagonismo/emprego** por parte de quem opera hoje nas operadoras.
**Fato — proposta de valor comunicando "de menos"** (não trazendo o impacto de resultado financeiro amplo, só a "parcela de campo").
**Fato — limite de escopo do produto hoje:** cobre gabinete + baterias, não cobre rede elétrica pública, cabeamento até a distribuidora, nem ar-condicionado — "a gente não tem esse know-how [...] a gente não tem capilaridade para ficar olhando para isso" (ex.: exigiria "polícia armada" em todo site, inviável por custo).
**Fato — limitação geográfica autoimposta:** não atuam na região Norte; concentração deliberada onde a RSM tem cobertura (~9 bases).

---

## 7. Ecossistema e mercado

**Fato — concorrentes citados:** Nilco (fornecedora de gabinete que também presta serviço, participou do mesmo BID Telefônica), Delta (fornecedora de fonte, idem) — sem sucesso comercial equivalente ao da Moura nesse volume.
**Fato — caso de concorrente que desistiu do contrato:** "teve um ano até que entrou e pediu para sair. Queria até vender os gabinetes para a gente, porque o contrato não estava bem [...] eles não botaram no contrato atualização do aluguel por IPCA [...] para ficar fixo durante 10 anos, o contrato vai valer um pó no final da vida." Ela atribui a resiliência da Moura nesse tipo de contrato à experiência histórica como fornecedora de montadoras.
**Fato — mercado de furto de bateria:** "é um mercado negro" — tanto chumbo (valor do metal) quanto lítio (reaproveitamento de células, "não tem aquele firewall da Tesla").

---

## 8. Visão de futuro

**Fato — modelo em desenho para sites legados ("sale and leaseback"):** "a gente também pode comprar para alugar [...] Eu compro esses ativos [...] porque eu tenho o CAPEX. Esse é um ponto positinho da Moura, ter CAPEX a um custo barato [...] fica com o comprometimento de me alugar."
**Fato — visão de monetização futura da plataforma:** "a gente entende que um dia ela pode ser vendida [...] modo software as a service [...] para a pessoa que está lá na gestão também conseguir olhar [...] até esse entendimento de plataforma e tudo que é produto Moura pode ser conectado a essa plataforma."
**Fato — outros produtos/segmentos do portfólio Moura Energia:** BES (já em operação, ~4 contratos de aluguel na época, modelo de arbitragem tarifária) e tração (empilhadeiras, ainda em desenho, não pronto para clientes).
**Fato — visão sobre segmentação futura de clientes de telecom:** hoje o foco é nas grandes por terem "as maiores infraestruturas [...] um volume muito grande", mas ela pondera que operadoras menores/Wi-Fi têm CAPEX menor e "pode ser que esse seja a cara da Moura [...] a gente é acostumado a ser capilarizado" — decisão final delegada a Thiago Mello.
