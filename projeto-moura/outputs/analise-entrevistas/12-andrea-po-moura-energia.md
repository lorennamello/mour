# Andrea — PO (Product Owner) do Moura Energia

**Papel:** Product Owner do "Energia como Serviço", responsável pela modelagem de novos negócios/produtos, orquestração entre áreas (fábrica, engenharia, comercial) e ponto focal do projeto de consultoria. Duas conversas: uma reunião de **planejamento/mapeamento de stakeholders** (curta, mais tática) e uma **imersão** extensa sobre histórico, modelo de negócio e contrato Vivo.

## Estrutura organizacional que ela descreve (reunião de planejamento)
- Moura Energia dividida em 3 partes: renováveis (fora do escopo de servitização), sistema de armazenamento (BES) e telecom.
- Daniel (financeiro) acompanha faturamento, sinergia contratual, furto e balanço do contrato já vigente; só entra na modelagem de **novos** negócios como validador, junto com o time dela.
- BES já é um "negócio de prateleira" (modelo padronizado, maturidade alta); Telecom ainda está em "modelo de prospecção" — cada operadora exige customização (não é um produto único, difere por operadora) — por isso o comercial de estacionárias (DCBE) ainda não assumiu isso integralmente.
- Mapeamento de quem entrevistar e por quê: Daniel (financeiro/visão helicóptero), Francisco (TI/plataforma), José Espinosa (operação/dia a dia, "no suado"), Josiele (interface fábrica↔Moura Energia, atendimento e requisitos), Spartacus (ex-diretor do ITEM, definiu a solução técnica junto com Thiago Mello — "CTO" informal do grupo), Thiago Mello (comercial, "dono"/relacionamento com executivos da Telefônica), Gustavo (visão de acionista/futuro, dor pessoal declarada: furto).
- Explica a cadeia de contato do cliente em caso de problema: Espinosa é o ponto de contato de operação; Aline/Karina para comercial; internamente, Josiele conecta a Moura Energia com a fábrica (ACMO).

## Origem do projeto (imersão)
- Quem trouxe a ideia foi **Thiago Mello**, percebendo oportunidade dentro da **TIM** (não Telefônica) — ele e Tiago Tasso estavam "na raiz" desde o começo, junto com Gustavo.
- Paralelamente ao trial da TIM, projetos de P&D no ITEM (chamados PID, "Face" e "Connect") desenvolveram o dispositivo de leitura de corrente/tensão/bateria e soluções antifurto — PID focado especificamente em telecom.
- Trial: 20 sites reais com a TIM (Greenfield e rooftop), sem cobrança de aluguel — modelo era "compramos os equipamentos, fazemos teste de 3 meses, depois vocês compram". Durante o trial houve um furto, e **todos os chamados de campo foram tratados pela Moura**, nenhum chegou à TIM — usado como prova de conceito de valor.
- TIM **comprou o ativo ao final do trial mas não contratou o serviço/aluguel** — segundo ela, por questão de CAPEX/EBITDA (a TIM não enxergava, na época, o benefício contábil do IFRS16 que reduz o impacto do CAPEX ao usar serviço — a Telefônica via esse valor, a TIM não). Também menciona confusão institucional na TIM sobre quem detém o CAPEX de infraestrutura (engenharia x outra área).
- Em paralelo, criou-se a engenharia de sistemas (dentro da Moura) e o cargo de PO — e o nome do projeto evoluiu de "Moras a Service" (MAS) para "Moura Energia como Serviço" (MEX), por sugestão de consultoria de marca (Silvio Meira/TDS).

## Estrutura societária/verticalização
- Moura Energia é uma **gestora de ativos**: compra CAPEX da fábrica (CMO/ACMO) e aluga. Se o cliente preferir comprar, a venda vai direto da fábrica — o comercial é único (não há comercial de venda separado do de servitização).
- RSM (Rede de Serviços Moura) é outra empresa do grupo, contratada pela Moura Energia para fazer instalação, comissionamento e O&M (Operação e Manutenção).
- Objetivo declarado: "que você foque no seu business" — a Moura assume o backup de energia de ponta a ponta.

## Como a Vivo entrou
- Após o trial da TIM, Thiago Mello teria usado o resultado como argumento de venda para outras operadoras ("estamos fazendo um negócio bom na TIM, por que vocês não fazem também?").
- A Telefônica abriu um edital (a Moura ajudou a construí-lo) focado inicialmente no gabinete **T2** (depois também T11).
- Negociação girou fortemente em torno de **quem assume a responsabilidade pelo furto** — inicialmente a Telefônica queria 100% de responsabilidade da Moura; a negociação (quase 1 ano até assinar) resultou num **cap de furto no contrato**.

## Números do contrato Telefônica (segundo Andrea)
- **1.950 sites** contratados no total (somando T2 e T11).
- Cap de furto contratual: cada site tem direito a **R$1.350/ano** de cobertura de furto (valor acumulado vira um "pool"); hoje a taxa real de furto já está **acima** desse valor (ela cita ~6% de índice de furto observado).
- Faturamento mensal: acima de R$1 milhão/mês (na época da entrevista), com mais de 400 sites instalados — ainda amortizando CAPEX inicial alto.
- Distribuição geográfica: hoje ~90% Greenfield / 10% rooftop (originalmente modelado como 85/15 — a proporção real é o inverso da premissa inicial de maior segurança). São Paulo concentra a maior fatia (na casa de 30%), seguido por Minas Gerais e Rio de Janeiro.
- Rollout contratual: até 3 anos (terminando em meados do ano seguinte à entrevista); prazo tende a ser aditivado/renegociado, prática comum nesse tipo de contrato segundo ela.
- Expansão geográfica limitada deliberadamente às regiões onde a RSM tem cobertura (hoje ~9 bases RSM); **não atuam na região Norte** por decisão própria (falta de RSM próxima torna operação inviável); atuam um pouco no Centro-Oeste (Brasília).

## Problemas de campo identificados (imersão)
- Conectividade: chip começou dedicado a uma operadora (Claro), causando problema quando o site ficava numa região sem cobertura daquela operadora — migraram para chip multi-operadora, o que gerou estouro de consumo de dados (de ~R$1 mil esperado para ~R$5 mil, por falta de calibração do IoT) — problema técnico que gera OPEX extra.
- Falta de geração automática de ticket quando ocorre furto sem detecção (etiquetagem/dado não confiável).
- Furto: cadeado Bluetooth serve para saber quem acessou (identifica "fogo amigo" — furto por técnico); grade (CAVE) ao redor do gabinete; mesmo assim há arrombamento com marreta etc. Rooftop tem menos furto (precisa identificar-se para subir no prédio), mas é só 10% dos sites hoje.

## Proposta de valor (elevator pitch dela)
- Backup de energia contínuo, mantém SLAs contratuais, cumpre regras regulatórias (Anatel), zero CAPEX de investimento para o cliente, redução de O&M própria, foco no core business.
- Autocrítica: acha que hoje comunicam menos do que poderiam — falam da "parcela de campo" mas não trazem à tona o impacto no **resultado financeiro** amplo do cliente (parcela de negócio ponto a ponto).
- Reconhece incerteza sobre se estão falando com as pessoas certas dentro das operadoras (quem decide de cima ou quem sofre na operação — que pode temer perder o emprego).

## Escopo e limites do que é garantido
- Escopo do "backup de energia" hoje é o gabinete + baterias; **não inclui rede elétrica pública, cabeamento da distribuidora, nem ar-condicionado** (avaliado como oportunidade de manutenção maior, não priorizado) — a Moura reconhece que não tem know-how/capilaridade para ir além disso ainda (ex.: gerador não é escopo hoje, apesar de já ter sido perguntado por um cliente).

## Modelo de compra do legado ("Sale and Leaseback")
- Modelo em desenho (inclusive com a própria Telefônica): comprar o ativo/parque já existente do cliente (ex.: 500 sites) e devolver como aluguel — a Moura tem CAPEX barato como vantagem competitiva para viabilizar isso.

## Operadoras pequenas / outros segmentos
- Não há exclusão de operadoras pequenas (ex.: participaram de um BID da Algar com apenas 75 sites) — estão no momento de "aprender", não de recusar.
- Segmento de Wi-Fi/ISPs menores tem CAPEX menor mas exige monitoramento proporcionalmente maior — ainda não desenhado.
- Fora de telecom: BES já está em operação/aluguel (~4 contratos na época), modelo de arbitragem tarifária (carrega fora de ponta, descarrega na ponta); tração (empilhadeiras) em desenvolvimento, ainda não pronto para clientes.

## Concorrência (visão dela)
- Concorrentes diretos de serviço completo: praticamente nenhum no nível de volume da Moura — cita Nilco (fornecedora de gabinete que também presta serviço) e Delta (fornecedora de fonte) como players que disputaram o mesmo BID da Telefônica, mas sem sucesso comercial equivalente.
- Um concorrente teria entrado num contrato e desistido por erro de modelagem (sem reajuste por IPCA no contrato, por exemplo) — reforça a vantagem da experiência da Moura com contratos longos (ex-fornecedora de montadoras).
