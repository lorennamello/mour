# Hipóteses de Product-Market Fit para testar na Fase 2
### Da imersão interna (Fase 1) para o roteiro de entrevistas com as operadoras

**Objetivo:** para cada crença/hipótese identificada internamente sobre por que a servitização "encaixa" (ou não) para os clientes, propor uma ideia de proposta de valor concreta — testável na conversa com as operadoras — em vez de apenas capturar dores.

**Metodologia desta versão:** cada hipótese foi cruzada (1) com o desafio que a própria Moura enfrentaria para entregar essa ideia, extraído das 15 transcrições internas, e (2) com um caso real de mercado comparável, via pesquisa externa. As ideias abaixo tentam já nascer resolvendo o desafio interno identificado, não só a dor do cliente.

**Nota metodológica:** as hipóteses 4 e 5 são marcadas na planilha-fonte como **divergentes entre si** (vieram de dois entrevistados diferentes — Yasmin e Espinosa — com leituras opostas sobre o que o cliente valoriza mais). A Fase 2 não deve testá-las de forma isolada: o objetivo é descobrir qual domina, possivelmente variando por operadora ou por interlocutor.

---

## 1. Recompra dos ativos / site legado

**Desafio interno (Moura):** a empresa já sofre com o alto CAPEX necessário para fabricar gabinetes antes de começar a faturar (Francisco). Buy-and-lease-back soma *mais* CAPEX em cima disso — comprar de volta o ativo do cliente. Pior: José Espinoza trata sites legados como "sucata" na operação real, e Thiago revela que, pelo menos com a Telefônica, o cliente **já tem canal próprio de venda dessa sucata** — recomprar pode não ser percebido como valor novo.

**Precedente de mercado:** em sale-leaseback, o ativo é avaliado a "valor de liquidação" (leilão), tipicamente 70-80% do valor aceito pelo financiador — sempre bem abaixo do que o dono do ativo acha que vale. É exatamente o gap que gera frustração no cliente.

**Ideias refinadas:**
- **Recompra faseada/em lotes**, priorizando sites de maior risco, em vez do parque legado inteiro de uma vez — escalona o desembolso de caixa da Moura.
- **Crédito abatido no aluguel** em vez de pagamento à vista — o valor residual vira desconto nas primeiras mensalidades, sem desembolso imediato.
- **Ponte via hipótese 4**: entrar só com telemetria nos sites legados (sem comprar nada), migrando para o pacote completo quando o hardware antigo estiver perto do fim de vida natural.

**Como testar:** perguntar ao cliente qual valor ele *esperaria* receber pela recompra — e comparar com o valor residual que a Moura consegue pagar de forma sustentável, antes de desenhar a proposta.

## 2. Medo de perder o domínio da operação (depender 100% da Moura)

**Desafio interno:** o prazo de 10 anos não é arbitrário — está ligado à vida útil da bateria de lítio *e* ao prazo do financiamento que sustenta o negócio (Time do Financeiro). Encurtar o prazo ou dar saída fácil quebra a conta financeira já apertada.

**Precedente de mercado:** cláusulas de saída em contratos de outsourcing de TI são padrão de mercado — cobrem *transition assistance*, devolução de dados/ativos e handover documentado. Sem isso, o fornecedor não tem incentivo a cooperar (o próprio medo do cliente).

**Ideias refinadas:**
- Cláusula de saída **paga, não gratuita** — rescisão antecipada com multa/reembolso de CAPEX residual decrescente ao longo dos 10 anos.
- Piloto formal (12-24 meses) antes do contrato de 10 anos, em vez de reversibilidade embutida nele.
- "Operação assistida": Moura cuida do físico, mas cliente mantém pontos de veto em decisões críticas.

**Como testar:** "o que precisaria estar no contrato para vocês assinarem 10 anos com conforto?" — comparar com o que é financeiramente viável para a Moura.

## 3. Pensam apenas no preço da bateria (hard saving)

**Desafio interno:** Aline e Thiago admitem que a Moura nunca teve uma apresentação de TCO robusta — o comercial "gagueja" na hora de provar o ganho matematicamente. O problema não é só a crença do cliente, é a ausência da ferramenta.

**Precedente de mercado:** a melhor prática de TCO em vendas B2B complexas é co-criar a calculadora com o cliente (operações, financeiro, compras), não entregar pronta de fora para dentro.

**Ideia refinada:** levar uma calculadora de TCO em branco, que o time de Compras/Financeiro do cliente preenche ao vivo com os próprios dados dele (histórico de furto, custo de visita técnica) — vira ferramenta de descoberta conjunta, não discurso.

**Como testar:** a reação e as perguntas que surgem durante o preenchimento ao vivo revelam se "hard saving" é crença real ou ausência de ferramenta melhor.

## 4. Pagariam para ter os dados inteligentes

**Desafio interno:** a plataforma hoje é, nas palavras da própria Vanessa, um "MVP que virou produção" — sem 100% de confiabilidade, com dados que exigem "trabalho arqueológico" (Tarcísio). Vender dados como produto isolado expõe essa fragilidade que hoje fica escondida dentro do pacote completo.

**Precedente de mercado:** retrofit de IoT em equipamento existente (*brownfield*) é categoria de mercado já estabelecida, considerada caminho de menor custo/risco para digitalização — valida a categoria, mas a literatura enfatiza que o valor depende inteiramente da confiabilidade do dado.

**Ideia refinada:** o exemplo original (Connect Plus em hardware existente do cliente), mas com escopo restrito a poucos alarmes de altíssima confiabilidade (porta aberta, queda de energia) em vez do pacote completo de telemetria.

**Como testar:** perguntar isoladamente — "se a Moura só cuidasse dos dados do que vocês já têm instalado, isso teria valor?" — sem mencionar hardware, para separar essa dor da dor física (hipótese 5).

## 5. Pensam apenas na segurança física do produto

**Desafio interno:** o mecanismo de furto já mapeado (cadeado Bluetooth serrado sem acionar o alarme, "fogo amigo" de técnicos do setor) mostra que a Moura ainda não resolveu isso nem para si mesma.

**Precedente de mercado:** tags de rastreamento cobertas (BLE oculto + decoy visível) recuperam mais de 85% dos ativos, contra 20-25% de rastreadores só visíveis — o cadeado visível que a Moura usa hoje é a arquitetura mais fraca da categoria.

**Ideias refinadas:**
- Produto avulso de rastreamento coberto, não o cadeado atual — resultado de recuperação comprovado no mercado.
- "Garantia de reposição com SLA" em vez de prevenção — transfere o risco financeiro sem prometer que o furto não vai acontecer.

**Como testar (junto com a 4):** "o que importa mais — nunca ser surpreendido, ou nunca ficar no prejuízo quando acontece?"

## 6. Vendendo da forma errada (apresentação)

**Desafio interno:** Josiele reconhece que a Moura não tem especialista em marketing B2B complexo — testar "dois discursos" pressupõe ter pelo menos dois discursos bem construídos, e hoje não há nenhum.

**Ideia refinada:** em vez de discurso, testar o meio — a calculadora de TCO da hipótese 3 como o próprio discurso, deixando o cliente construir a conclusão junto em vez de assistir a um pitch.

## 7. Vendendo para o stakeholder interno errado

**Desafio interno:** Karina já documentou o erro (vendeu para Operações) e agora tenta ir direto ao Board da TIM — mas a Moura não tem relacionamento estabelecido nesse nível em nenhuma operadora além da Vivo.

**Precedente de mercado:** negociações single-threaded fecham a 5%, multi-threaded a 30%; negócios engajando 3+ áreas fecham a 44% vs. 28% com uma área só. A resposta não é trocar um alvo errado por outro único alvo — é multi-thread.

**Ideia refinada:** engajar simultaneamente Board + Compras + Engenharia + uma Regional, com mensagem adaptada por papel.

**Como testar:** entrevistar as 4-5 áreas da mesma operadora na Fase 2 e comparar se a mensagem que funciona é diferente por papel.

## 8. Perda de credibilidade (entregando mal outros serviços da Moura)

**Desafio interno:** o time comercial teve 100% de turnover e ainda está "resgatando e-mails perdidos" — um piloto com SLA público exigiria uma capacidade operacional que a própria Moura reconhece não ter 100% hoje.

**Precedente de mercado:** recuperação de confiança B2B depende de "prova, não promessa" — mostrar estruturalmente que a mesma falha foi fechada.

**Ideia refinada:** piloto pequeno com dashboard de SLA visível ao cliente em tempo real (não relatório mensal) — a transparência do dado, não o tamanho do piloto, reconstrói confiança.

**Como testar:** perguntar à Claro (relação mais desgastada) qual seria o "sinal mínimo" que reconstruiria confiança, e comparar com a capacidade real de SLA da Moura hoje.

## 9. As operadoras não têm CAPEX / querem reduzir CAPEX *(hipótese-mãe)*

**Desafio interno:** a Moura já tem "receita fixa, custo variável" (frete, furto) — qualquer modelo de preço variável para o cliente pode piorar ainda mais esse descasamento do lado da Moura.

**Precedente de mercado:** energia como serviço para torres de telecom já é modelo comprovado em mercados emergentes — MTN cortou 30% do gasto com diesel via solar no Sudão do Sul; Airtel Africa + ENGIE Energy Access reduziram uso de diesel em mais de 50% na Zâmbia e Congo, no mesmo papel de parceiro especializado que a Moura quer ocupar.

**Ideia refinada:** testar um modelo fixo com piso e teto (banda de preço) — dá previsibilidade de receita para a Moura sem ser 100% variável, mas oferece elasticidade percebida ao cliente.

**Como testar:** citar os cases reais (MTN, Airtel/ENGIE) como abertura da conversa financeira — testar se cases internacionais mudam a receptividade ao argumento.

---

*Fonte interna: planilha/PDF `Moura_Telecom_Phase_1__Interviews.xlsx`, aba Hipóteses, cruzada com as 15 transcrições de entrevistas internas.*

*Fontes externas consultadas:*
- [Africa's cellphone towers turn to solar as diesel costs surge](https://abcnews.com/amp/International/wireStory/africas-cellphone-towers-turn-solar-diesel-costs-surge-132593954)
- [Sale Leaseback Financing: The Hidden Capital Strategy](https://medium.com/@stanprokop/sale-leaseback-financing-the-hidden-capital-strategy-273be3cc6fc8)
- [Pondering the Possibility of Sale-leaseback Financing](https://www.apslaw.com/construction-industry-advisor/2025/09/24/pondering-the-possibility-of-sale-leaseback-financing/)
- [Brownfield IoT: Retrofitting Legacy Industrial Machinery for Predictive Maintenance](https://intechhouse.com/blog/brownfield-iot-retrofitting-legacy-industrial-machinery-for-predictive-maintenance)
- [Vendor Lock-In: A Procurement Problem, Not a Technical One](https://domenicomonteleone.com/vendor-lock-in-procurement-decision/)
- [Vendor Lock-In Risks in Outsourcing: 9 Smart Strategies](https://unity-connect.com/our-resources/bpo-learning-center/vendor-lock-in-risks-in-outsourcing/)
- [Covert GPS Tracking Stickers for Anti-Theft and Asset Recovery](https://gpx.co/blog/covert-gps-tracking-sticker-anti-theft/)
- [How GPS tracking helps recover assets and prevent theft](https://www.samsara.com/blog/mitigate-theft-with-asset-tag)
- [Multi-Threading in Sales: The Strategy That 6x Your Win Rate](https://salesmotion.io/blog/multi-threading-sales-strategy)
- [5 important elements of stakeholder mapping in B2B sales](https://inaccord.com/blog-posts/5-important-elements-of-stakeholder-mapping-in-b2b-sales)
- [Total Cost of Ownership (TCO) - B2B Deal Pricing](https://umbrex.com/resources/frameworks/pricing-frameworks/total-cost-of-ownership-tco/)
- [Vendor Breach Recovery: How To Earn Back Client Trust](https://www.forbes.com/councils/forbestechcouncil/2026/06/29/vendor-breach-recovery-how-to-earn-back-client-trust/)
- [Why Pilot Programs Are a Best Practice for B2B SaaS](https://partnerstack.com/articles/pilot-programs-testing-learning-b2b-saas)
