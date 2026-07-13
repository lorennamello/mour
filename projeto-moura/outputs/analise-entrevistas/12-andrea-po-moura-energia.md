# Andrea — PO (Product Owner) do Moura Energia

**Papel:** Product Owner do "Energia como Serviço", responsável pela modelagem de novos negócios/produtos, orquestração entre áreas (fábrica, engenharia, comercial) e ponto focal do projeto de consultoria. Duas conversas: uma reunião de planejamento/mapeamento de stakeholders (curta, mais tática) e uma imersão extensa sobre histórico, modelo de negócio e contrato Vivo.

---

## 1. Proposta de valor

**O que a Moura Energia entrega (Fato — elevator pitch, quando pedido diretamente):** "a gente presta um serviço de backup contínuo, de backup de energia contínuo [...] a gente não deixa a tua disponibilidade de serviço parar. Com isso [...] a gente mantém seus SLA necessários, a gente cumpre regras regulamentares e a gente te proporciona zero CAPEX de investimento [...] a redução de OIM [...] e o foco no core business."

**Problema que resolve (Fato):** continuidade de energia para cumprir regulação Anatel; gestão de furto, manutenção e CAPEX.

**Clientes (Fato):** Telefônica (contrato ativo), TIM (trial sem conversão), Algar (BID pequeno, em aprendizado).

**Valor percebido (Fato — autocrítica imediata sobre o próprio pitch):** "Isso pode não estar ideal. Essa é a crítica que a gente sempre faz dentro de casa. Será que é isso mesmo que a telefônica tem que ouvir? Será que a gente está acertando?" Reformulação: "a gente está enxergando uma parcela da operadora, que é a parcela de campo, mas a gente não está olhando a parcela de que isso dá no resultado [...] Acho que a gente está falando de menos."

**Diferenciais (Fato):** analogia usada — "Se eu sou cliente da Vivo [...] se falta energia, eu vou ter um problema. Então, quem está me garantindo energia? A Moura. Então, se a Moura está bem, meu cliente também está bem."

**Interpretação:** Andrea é quem mais reconhece explicitamente que o discurso de valor atual está incompleto — ela não apenas descreve o pitch, mas audita sua própria eficácia em tempo real durante a entrevista, sugerindo autoconsciência institucional do problema, mesmo sem tê-lo resolvido.

---

## 2. Desafios internos

### Na área dela (Produto/PO)
- **Problema:** Telecom ainda não é um "produto de prateleira" como o BES. **Impacto:** cada operadora exige um desenho customizado, atrasando escala. **Quote:** "Quando a gente vai para a telecom, é algo totalmente não padronizável [...] a telefônica tem um padrão, a TIM tem outro padrão [...] tem muita customização que o comercial [...] ainda não assumiu."
- **Problema:** decisão técnica de conectividade não calibrada gerou estouro de custo. **Impacto:** OPEX 5x acima do esperado num primeiro momento. **Quote:** "a gente começou com o chip da Claro, aí depois [...] a gente tem que ir para a multi-operadora [...] teve o estouro de dados, porque o IoT não estava calibrado [...] estava dando cinco mil reais" (esperavam ~mil).
- **Problema:** falha de geração automática de ticket em furtos. **Impacto:** eventos não registrados formalmente na plataforma. **Quote:** "às vezes, acontece do site ser furtado e não gerar um ticket [...] na plataforma da gente. Então, isso é um problema também que está tendo."

### Percepção sobre desafios de outras áreas
- **Problema (comercial):** dúvida sobre estar falando com os stakeholders certos. **Impacto:** conversas que não avançam. **Quote:** "será que a gente está acertando, a gente está falando com a pessoa correta mesmo. Quem é que define isso? Quem vem de cima ou quem vem de baixo?"
- **Problema (cliente/operação):** percepção de resistência da operação do cliente. **Impacto:** barreira à adoção. **Quote:** "quem está na operação vai dizer assim, se eu botar esses caras aí, eu vou perder meu emprego [...] E o cara de cima, ele diz assim, opa, isso aqui eu vou ter uma otimização."
- **Problema (financeiro/modelagem):** cap de furto do contrato Telefônica já sendo superado na prática. **Impacto:** risco de custo não coberto. **Quote:** "o nosso [índice de furto] já está em torno de 6%[.] Mas hoje, no contrato [...] anualmente, cada site tem direito a R$1.350 de furto [...] esse valor já está acima [do previsto]."
- **Problema (operação/instalação em rooftop):** custo de guindaste cresce exponencialmente por andar. **Impacto:** dificuldade de modelagem precisa. **Quote:** "a cada 15 andares, o valor do guincho, do guindaste, vai aumentando meio que exponencialmente [...] Para modelar [...] é meio que impossível."

---

## 3. Áreas internas

**Daniel (financeiro):**
- Papel: "toda a parte de negócios, de contrato, de pagamento, de faturamento [...] Quando é para novos negócios [...] a área de PO se envolve para modelar [...] o Daniel é como se fosse também um validador dessa modelagem."
- Dependência: ele não tem responsabilidade na modelagem de novos negócios, só valida.

**José Espinosa (operação):**
- Papel: "a operação do contrato, a execução [...] Ele já trabalhou bastante [...] mais de 10 anos, na TIM."

**Josiele:**
- Papel: "faz a gestão do contrato [...] atendimento ao cliente [...] o cliente é Moro Energia [...] alinha os requisitos com a fábrica, alinha os requisitos com a engenharia, faz tudo de dentro de casa." Está no DCBE (fábrica/ACMO), não na Moura Energia; papel "mais de interface [...] mais de marketing do que de engenharia."

**Spartacus (ex-diretor do ITEM):**
- Papel: "ele é meio que o CTO da gente [...] tudo que é técnico passa por ele [...] ele definiu junto com o Marcos Malveira a solução técnica [...] ele desenhou junto com o Thiago Melo a solução."

**Francisco (TI):**
- Papel: "visão dele é mais estrutural de plataforma [...] se a gente um dia vai querer vender essa plataforma para a operadora."

**Thiago Mello:**
- Papel: "ele é o comercial [...] ele que foi atrás dessa [...] esse negócio [...] tem contato das pessoas [...] a pessoa que vocês precisam mais explorar [...] ele nunca vai ser só um respondedor de perguntas."

**Gustavo:**
- Papel: "olha para frente [...] uma dor dele, que eu sei, é furto."

**Interpretação:** o mapeamento de Andrea revela uma estrutura de governança altamente pessoal/informal — cada área tem um "dono" claro, mas a integração entre eles depende fortemente de quem "costura" manualmente essas pontas, e ela mesma se posiciona como essa costureira central, consistente com relatos de outros entrevistados sobre gargalos de coordenação.

---

## 4. Modelo comercial

**Como surgem oportunidades (Fato):** ideia trazida por Thiago Mello, oportunidade percebida primeiro na TIM; trial de 20 sites reais (Greenfield e rooftop), sem cobrança — "compra ao final se der certo."

**Como acontece a venda (Fato — resultado do trial TIM):** durante os 3 meses, houve um furto e "não se teve nenhum chamado para telefone, para a TIM. Todos esses chamados [...] foram todos para Moro" — usado como prova de conceito; ainda assim, a **TIM comprou o ativo, não contratou o serviço**.

**Quem vende e influencia (Fato):** Thiago Mello lidera; ela modela o negócio junto com Carol, Maria Cecília, validado por Gustavo e Tiago Tasso.

**Argumentos que funcionam (Fato — caso Telefônica):** Thiago Mello teria usado o resultado do trial TIM como argumento comercial com a Telefônica, que abriu um edital construído em parceria com a Moura.

**Argumentos que não funcionam / objeções (Fato — hipótese dela, a confirmar):** TIM não converteu por questão de CAPEX/EBITDA (não percebeu o benefício do IFRS16 que a Telefônica viu); possível confusão institucional na TIM sobre quem detém o orçamento de infraestrutura.

**Diferenças entre clientes (Fato):** negociação do contrato Telefônica girou fortemente em torno de quem assume o risco de furto — inicialmente a Telefônica queria 100% de responsabilidade da Moura; negociação (quase 1 ano) resultou num cap contratual.

---

## 5. Visão sobre os clientes

**Perfil (Fato):** Telefônica — relação "muito colaborativa", elogios de tempo de resposta e prontidão; TIM — interessada em inovação, mas travada por questões contábeis/institucionais internas.

**Comportamento (Fato):** segmentação Greenfield x rooftop com implicação direta na exposição a furto — hoje ~90% Greenfield / ~10% rooftop, inverso da modelagem original (85%/15%), significando mais exposição ao risco de furto do que planejado.

**Maturidade (Fato):** clientes pequenos não são excluídos — participaram de um BID da Algar com apenas 75 sites, "a gente não deixou de oferecer [...] a gente está no momento de entender."

---

## 6. Barreiras de expansão

- **Internas:** proposta de valor comunicando "de menos" (não trazendo o impacto de resultado financeiro amplo, só a "parcela de campo"); dúvida sobre estar falando com as pessoas certas.
- **Externas/Clientes:** medo de perda de protagonismo/emprego por parte de quem opera hoje nas operadoras.
- **Mercado (escopo do produto):** limite de escopo hoje — cobre gabinete + baterias, não cobre rede elétrica pública, cabeamento até a distribuidora, nem ar-condicionado — "a gente não tem esse know-how [...] a gente não tem capilaridade para ficar olhando para isso" (exigiria "polícia armada" em todo site, inviável por custo).
- **Geográficas:** limitação geográfica autoimposta — não atuam na região Norte; concentração deliberada onde a RSM tem cobertura (~9 bases).

---

## 7. Ecossistema e mercado

**Concorrência (Fato):** Nilco (fornecedora de gabinete que também presta serviço) e Delta (fornecedora de fonte) — ambos participaram do mesmo BID Telefônica, sem sucesso comercial equivalente ao da Moura nesse volume. Caso de concorrente que desistiu do contrato: "teve um ano até que entrou e pediu para sair. Queria até vender os gabinetes para a gente, porque o contrato não estava bem [...] eles não botaram no contrato atualização do aluguel por IPCA."

**Posicionamento da Moura Energia (Fato):** ela atribui a resiliência da Moura nesse tipo de contrato à experiência histórica como fornecedora de montadoras.

**Mercado paralelo (Fato):** furto de bateria "é um mercado negro" — tanto chumbo (valor do metal) quanto lítio (reaproveitamento de células, "não tem aquele firewall da Tesla").

*Não abordado: TowerCos diretamente (fora do contexto de furto), integradores, fornecedores de tecnologia.*

---

## 8. Visão de futuro

**Próximos passos (Fato — modelo em desenho para sites legados, "sale and leaseback"):** "a gente também pode comprar para alugar [...] Eu compro esses ativos [...] porque eu tenho o CAPEX. Esse é um ponto positinho da Moura, ter CAPEX a um custo barato."

**Novos modelos (Fato — monetização futura da plataforma):** "a gente entende que um dia ela pode ser vendida [...] modo software as a service [...] para a pessoa que está lá na gestão também conseguir olhar."

**Novos mercados (Fato):** BES (já em operação, ~4 contratos de aluguel na época, modelo de arbitragem tarifária) e tração (empilhadeiras, ainda em desenho, não pronto para clientes).

**Prioridades (Fato):** hoje o foco é nas grandes operadoras por terem "as maiores infraestruturas [...] um volume muito grande", mas pondera que operadoras menores/Wi-Fi têm CAPEX menor e "pode ser que esse seja a cara da Moura [...] a gente é acostumado a ser capilarizado" — decisão final delegada a Thiago Mello.

---

## 9. Hipóteses para validação (Fase 2 — com operadoras)

| O que o time interno acredita (opinião de Andrea) | Hipótese estruturada para testar com o mercado |
|---|---|
| Hoje comunicam "de menos" o valor — falam da "parcela de campo", mas não trazem à tona o impacto no resultado financeiro amplo do cliente. | As operadoras podem já estar cientes do impacto financeiro amplo, mas o real obstáculo pode ser que **o time que decide (financeiro/RI) não é o mesmo que avalia o piloto tecnicamente** — testar quem, de fato, aprova esse tipo de contrato de ponta a ponta em cada operadora. |
| TIM comprou o ativo em vez de alugar por questão de CAPEX/EBITDA — mas ela mesma reconhece incerteza. | A decisão pode ter sido tomada por um comitê financeiro que **nunca recebeu diretamente** o argumento de IFRS16/EBITDA usado com sucesso na Telefônica — testar apresentando esse argumento especificamente ao CFO/comitê financeiro da TIM. |
| Quem opera hoje no cliente teme perder o emprego, enquanto quem está "de cima" vê a otimização como ganho. | Pode haver **dois níveis de decisão com incentivos opostos** dentro da mesma operadora — testar entrevistando separadamente alguém do nível operacional e alguém do nível estratégico da mesma operadora. |
| Escopo restrito a gabinete + bateria é aceito pelo cliente sem atrito. | Pode haver demanda latente por ampliar esse escopo nunca formalmente sondada — ela relata que um cliente já perguntou sobre gerador em uma reunião — testar diretamente se ampliação de escopo é fator decisório para fechar/expandir contratos. |

---

## 10. Pessoas-chave para falar dentro do cliente (operadora)

**Já conversados, segundo ela:**
- **Telefônica** — Espinosa relata contato recente com "o responsável da Telefônica" — resultado positivo (reconhecimento do bom desempenho, mais de 400 sites, ~6% de furto considerado dentro do aceitável pelo cliente).
- **TIM** — trial de 20 sites reais; resultado: TIM comprou o ativo, não contratou o serviço.
- **Algar** — BID com 75 sites, ainda em fase de aprendizado, sem fechamento.

**Não conversados / lacuna identificada por ela mesma:**
- Pergunta central em aberto: "Quem é que define isso? Quem vem de cima ou quem vem de baixo?" — sem mapeamento sistemático de decisor final vs. influenciador de base.
- Não identifica um comitê financeiro/CFO específico em nenhuma operadora como interlocutor já testado.

---

## 11. Outros insights

- **Ela é a entrevistada que melhor articula a governança interna do projeto (quem é quem, quem depende de quem)** — o mapeamento dela na reunião de planejamento é a fonte mais confiável para reconstituir o organograma funcional real do Moura Energia, cruzando com o que os próprios citados (Daniel, Espinosa, Francisco, Thiago Mello) confirmam em suas entrevistas.
- **A autoauditoria em tempo real do próprio pitch de valor** (seção 1) é um comportamento não observado em nenhum outro entrevistado — sugere que ela é, hoje, a pessoa dentro da Moura Energia mais consciente da lacuna entre discurso comercial e necessidade real de reformulação.
