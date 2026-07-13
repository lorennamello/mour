# Visão Consolidada — Produto/Serviço Moura Energia (Telecom) e Contrato com a Vivo (Telefônica)

> Documento que cruza as falas de todos os 12 entrevistados sobre o que é o produto/serviço Moura Energia em Telecom e sobre o contrato vigente com a Vivo/Telefônica. Cada ponto é atribuído à(s) fonte(s) que o mencionou, para preservar a granularidade e permitir checar a origem de cada informação. Onde há divergência ou informação não confirmada entre fontes, isso é sinalizado explicitamente.

---

## 1. O que é o produto/serviço, em essência

**Definição central (convergência entre quase todos):** a Moura Energia vende **backup de energia contínuo como serviço** para sites de telecomunicações — não vende mais bateria avulsa, e sim a solução completa: gabinete + bateria + fonte/retificador + monitoramento + manutenção, em modelo de aluguel de longo prazo (10 anos no caso Telefônica), com a Moura assumindo o ativo, o risco de furto (até um teto) e a responsabilidade operacional.

- **Analogia mais usada** (Thiago Mello): hoje a Moura "aluga a caixa d'água, não garante o banho" — ou seja, fornece um backup por tempo determinado (as horas contratadas), não energia ilimitada; ele vê como necessidade futura evoluir para garantir disponibilidade de fato.
- **Frase-síntese do valor** (Aline Souza): "faz o que você é bom e deixa a energia que a gente resolve".
- **Frase-síntese** (Josi): o objetivo é o cliente "não ter que se preocupar" com o site.
- **Frase-síntese** (Consultor de Projetos/Operação Vivo): o diferencial não está no produto físico (que é o mesmo há 20 anos, especificado pelo próprio cliente), mas no **"como"** — qualidade de execução, comunicação proativa, velocidade.
- **Frase-síntese** (Espinosa): "eu sou especialista no que eu faço e deixo você ser especialista no que você faz" (variação também usada por Driele).

## 2. Como o negócio nasceu (linha do tempo cruzada)

| Momento | O que aconteceu | Fontes |
|---|---|---|
| ~1998–1999 | Moura entra no mercado de bateria para telecom (importação, depois fabricação própria); chega a ~86-90% de market share | Thiago Mello, Gustavo Moura |
| ~2009-2010 | Surgimento das torreiras; operadoras provocam a Moura a assumir backup de energia, mas Moura ainda não tinha estrutura | Thiago Mello |
| ~2018-2019 | Transição chumbo→lítio; Moura passa a instalar também o retificador (parceria com a Delta) | Thiago Mello |
| 2022 | Aproximação com a AWS; imersão com metodologia "working backwards" define os 3 pilares do produto (hardware, firmware, software) | Francisco (TI) |
| 2022 (paralelo) | ITEM desenvolve os PIDs "Face" e "Connect" (leitura de corrente/tensão/bateria) | Andrea |
| Antes do trial | Protótipos "Moura Connect" (empilhadeiras) e "Moura Lock/Moralonqui" (trava antifurto, não avançou) — CNPJ Moura Energia ainda não existia | Vanessa |
| ~2022-2023 | Trial/POC real com a **TIM**: 20 sites (Greenfield e rooftop), sem cobrança — "compra ao final se der certo" | Andrea, Vanessa, Daniel Garcia, José Espinosa, Josi |
| Resultado do trial TIM | TIM **comprou o ativo mas não contratou o serviço/aluguel** | Andrea, Gustavo, Daniel Garcia |
| 2023 | Nasce "Moura as a Service" (MAS), depois renomeado "Moura Energia como Serviço" (MEX) por sugestão de consultoria de marca (Silvio Meira/TDS) | Andrea, Vanessa |
| 2023-2024 | Estruturação formal da Moura Energia (CNPJ próprio), engenharia de sistemas, cargo de PO criado | Andrea |
| 2024 | Contrato assinado com a **Telefônica (Vivo)** — depois de quase 1 ano de negociação | Andrea, Aline Souza |
| Out/2024 | Primeiro site instalado no contrato Vivo | Daniel Garcia |
| Meados de 2025 | Aditivo contratual libera o gabinete T11 (antes só T2) | Daniel Garcia |

### Por que TIM comprou em vez de alugar, mas a Telefônica alugou
- **Andrea**: a Telefônica enxergava o benefício contábil do **IFRS16** (uso de serviço não afeta tanto o resultado/EBITDA quanto comprar); a TIM não via esse valor da mesma forma. Também havia confusão institucional na TIM sobre quem detinha o CAPEX de infraestrutura.
- **Gustavo Moura**: reforça que a TIM "apertou o preço" e não percebeu valor suficiente; destaca que foi **Luiz Melo** (ex-diretor) quem identificou que a Telefônica já tinha um processo aberto e que a Moura não estava participando — "a Telefônica nos comprou", não o inverso.
- **Thiago Mello**: acrescenta que TIM e Telefônica pressionaram as torreiras a assumir esse risco, mas as torreiras resistiram (modelo delas exige estabilidade de custo para captar capital barato) — abrindo espaço para a Moura entrar diretamente.
- **Josi**: TIM entende energia como "um negocinho bem pequenininho" perto do core, mas ainda assim resiste a delegar.

## 3. Arquitetura do produto (físico + digital)

### Estrutura física (gabinete)
- **Componentes** (Técnico/explicação do gabinete, Vanessa): fonte (Delta ou NRSys homologadas hoje; Delta parou de fornecer), quadro de disjuntores, banco de baterias (chumbo 12V ou lítio 48V), grade/CAVE de proteção, cadeado com trava Bluetooth.
- **Modelos**: **T2** (duas portas lado a lado) e **T11** (uma porta em cima da outra) — nomenclatura usada por quase todos; contrato Telefônica começou só com T2, aditivo depois liberou T11 (Daniel Garcia, Andrea).
- Cada gabinete normalmente atende **uma operadora**; em sites compartilhados (torreira) pode haver vários gabinetes lado a lado, um por operadora (Técnico).
- Gabinete tem 2 portas de acesso: uma da Moura (bateria) e uma da operadora (equipamentos de comunicação) (Josi, Técnico, Vanessa).
- **Especificação do gabinete veio da própria Telefônica** (Thiago Mello, José Espinosa, Vanessa) — Moura seguiu a spec do cliente por não ter maturidade de engenharia própria na época; Telefônica paga por metro quadrado ocupado (não m³), o que já gerou negociações de otimização de altura do gabinete.
- Montagem/comissionamento acontece na Unidade 10, em Belo Jardim, antes de ir para campo (Vanessa, Técnico).

### Camada digital (plataforma/monitoramento)
- **Connect Plus**: dispositivo físico (essencialmente um Raspberry Pi encapsulado, parceria com a Esfera Labs) conectado à fonte, que coleta dados e envia via modem multi-operadora para a nuvem AWS (Vanessa, Francisco).
- Cada modelo de fonte/gabinete precisa de um processo de "homologação" (tradução de protocolo) no ITEM (Vanessa).
- **Duas plataformas coexistem**: a do ITEM (mais técnica/completa) e a "MEX", espelhamento com identidade visual própria feito pela TI da Moura a partir de requisitos da Moura Energia (Vanessa, Francisco).
- **Divisão de responsabilidade hoje**: ITEM ainda dá suporte de **hardware** (a transferência tecnológica de hardware para a Moura, diferente do BES, ainda não aconteceu); Moura Energia/TI cuidam mais do software/front-end (Vanessa, Francisco).
- Quem acessa a plataforma hoje: time de operação da Moura Energia (NOC, com apoio de terceiro), Espinosa e seu braço direito Tarcísio (Francisco, Vanessa, Andrea).
- A **operadora não tem acesso direto** à plataforma completa da Moura — recebe relatórios; ela só tem o espelhamento próprio que a fonte já gera nativamente para cumprir a Anatel (Francisco, Vanessa).

## 4. O que a plataforma entrega hoje x o que deveria entregar (visão operacional)

**O que já entrega bem hoje** (Consultor de Projetos/Vivo, Vanessa):
- Status online/offline em tempo real por site.
- Consumo de dados por site vs. franquia contratada.
- Status do cadeado (aberto/fechado).
- Histórico documental do site (implantação, pendências).
- Corrente, temperatura, tensão de barra, estado de carga.

**O que falta / é a maior lacuna:**
- **Autonomia do site** (quantas horas de backup restam) — a informação mais crítica, ligada a risco contratual/multa, não vem de forma direta e automática ("vomitada"); precisa ser garimpada (Consultor de Projetos, Vanessa).
- **Detecção confiável e em tempo real de furto** — hoje é inferida indiretamente pela fonte, não por um módulo de segurança dedicado (que fazia parte do plano original "Moura Cube" mas não foi implementado) (Vanessa, Consultor de Projetos).
- Alertas têm **falsos positivos e falsos negativos** (ex.: "porta aberta" sem ter sido aberta, ou não alerta quando algo realmente aconteceu) — causa raiz não totalmente mapeada (Consultor de Projetos).
- Em alguns casos, o cliente (Vivo) é quem avisa a Moura sobre um furto, não o contrário (Consultor de Projetos).

## 5. Causa raiz dos problemas técnicos: mais processo/instalação do que conectividade

- **Francisco (TI)**: o maior "vilão" da alarmística não é primariamente telecomunicação — é **erro de instalação em campo** (fonte instalada incorretamente). Estimativa dele: ~70-80 sites afetados (~30-35% na época).
- **Vanessa** confirma: já compartilhou com a equipe da consultoria um compilado de erros de campo (fio errado, energia não ligada, porta errada) e relata caso de bateria descarregada 100% porque o gabinete nunca foi ligado à energia.
- Aponta-se falta de **governança/handover** entre ITEM, engenharia e TI — quando dá problema, muitas vezes atribuem ao "Connect" (ITEM é chamado), mas na investigação frequentemente não é o Connect (Vanessa, Francisco).
- **Consumo de dados**: chip começou dedicado a uma operadora (Claro), causando falhas fora da área de cobertura dela; migrou para chip multi-operadora, mas isso gerou estouro de consumo de dados por falta de calibração (de ~R$1 mil esperado para ~R$5 mil, segundo Andrea) — ponto também levantado por Vanessa (modem comercial consome de forma "grosseira": >2GB/gabinete vs. ~15MB projetados numa versão otimizada testada em laboratório).

## 6. Furto/vandalismo — a dor mais citada por todos

- **Índice observado**: ~6-7% dos gabinetes vandalizados (Andrea cita ~6%; Consultor de Projetos cita ~7%).
- **Referência de modelagem original**: o modelo de negócio foi baseado em um percentual de **2%** (Consultor de Projetos) — ou seja, a realidade está bem acima do premissado.
- **Gustavo Moura** classifica o risco de furto como "sinal amarelo" em quantidade de eventos, mas ainda "verde" do ponto de vista financeiro (dentro do orçamento).
- **Cap contratual de furto** (ver seção 7) já estaria sendo superado proporcionalmente segundo Daniel Garcia.
- **Tipos de furto**: "fogo amigo" (o próprio técnico ou conhecido dele, identificável pelo cadeado Bluetooth que registra quem acessou) e furto "de fato" (arrombamento, mais comum em Greenfield) (Andrea, Espinosa, Aline Souza).
- **Rooftop tem muito menos furto** que Greenfield (precisa se identificar para subir no prédio) — mas rooftop é só ~10% dos sites hoje, mesmo tendo sido modelado originalmente como 15% (Andrea) — ou seja, a exposição ao risco de furto é maior do que a modelagem original previa.
- **Mitigações em curso**: reforço mecânico do gabinete, redimensionamento de energia (menos bateria instalada, complementando por demanda real via monitoramento — mudança em curso segundo Josi e Espinosa), estudo de rastreamento de bateria roubada, parceria com a polícia, isca de bateria, novo CAVE em desenvolvimento (Consultor de Projetos, Daniel Garcia).
- Mercado paralelo de baterias roubadas é significativo tanto para chumbo (valor do metal) quanto para lítio (reaproveitamento de células) (Andrea).

## 7. O contrato com a Vivo/Telefônica — dados e cláusulas (cruzamento de todas as fontes)

| Item | Valor/detalhe | Fonte(s) |
|---|---|---|
| Prazo do contrato | 10 anos | Andrea, Aline Souza |
| Total de sites contratados | 1.950 (Andrea) / "1.911" e "1.900" (outras fontes, arredondamentos) | Andrea, Daniel Garcia, Thiago Mello, Aline Souza |
| Sites instalados na época das entrevistas | ~400-415 | Consultor de Projetos (412), José Espinosa (415), Andrea, Daniel Garcia |
| Prazo de rollout | Até 3 anos (a partir do 1º site, out/2024); tende a precisar de aditivo de prazo, segundo Daniel Garcia | Daniel Garcia, Andrea |
| Ritmo de instalação | ~100 sites/mês (na época); ~80% do que a Vivo libera via sistema "Vivo Fly" | Francisco, Josi |
| Cap de furto | ~R$1.350/ano por site (valor acumulável em "pool" anual); segundo Daniel Garcia, já estouraram esse cap proporcionalmente (~R$100 mil acima do previsto para o nº de sites atual) — negociando emissão de nota de débito | Andrea, Daniel Garcia |
| % Greenfield x rooftop | ~90% Greenfield / ~10% rooftop (modelagem original previa 85%/15%, ou seja, mais rooftop e menos risco de furto do que a realidade) | Andrea, José Espinosa |
| Concentração geográfica | Maior parte em São Paulo (~30%), depois Minas Gerais, Rio de Janeiro; sem atuação na região Norte (decisão própria, falta de base RSM próxima); alguma presença no Centro-Oeste (Brasília) | Andrea, Daniel Garcia |
| Preço médio de aluguel | ~R$2.000/mês por site (fatores: depreciação, custo de financiamento, margem, "efeito medo"/furto) | Daniel Garcia |
| Faturamento do contrato | Acima de R$1 milhão/mês (na época) | Andrea |
| CAPEX investido | ~R$60 milhões (aproximado, na época) | Gustavo Moura |
| Financiamento | Project finance via BNB (Banco do Nordeste), taxa mais baixa | Daniel Garcia |
| Reajuste de preço | Existe cláusula de reajuste periódico — periodicidade não confirmada com precisão | Aline Souza |
| SLA de atendimento | Múltiplos níveis (4h mais crítico, 6h médio, 12h mais leve — a confirmar com o contrato); Vivo costuma ser flexível na prática | Consultor de Projetos |
| Multa por atraso de rollout | Confirmada — Moura pode ser notificada/multada se não cumprir prazo de instalação de lote | Aline Souza |
| Penalidade por indisponibilidade de energia ao cliente final | Não totalmente confirmada; possível rateio se a operadora for processada — Aline Souza não tinha certeza | Aline Souza |
| Cláusula de divulgação | Existe cláusula que permite divulgação ativa do case pela Moura em determinadas condições | Andrea |

> **Nota de divergência**: o número total de sites do contrato aparece como 1.950 (Andrea, com mais detalhe: "somando T2 e T11"), 1.911/1.900 (outras falas, provavelmente arredondamento coloquial). Vale confirmar o número exato em contrato antes de usar em relatório final.

## 8. Escopo do que é garantido (limites do produto)

- O escopo cobre o **gabinete completo**: estrutura, fonte, banco de baterias, cadeado, grade e monitoramento (Andrea, Espinosa, Vanessa).
- **Não inclui**: rede elétrica pública / cabeamento até a distribuidora, ar-condicionado (avaliado como oportunidade não priorizada), gerador (já perguntado por um cliente, mas fora do escopo hoje) (Andrea).
- Autonomia contratada é definida pelo **DEC** (tempo de backup: 2, 3 ou 4 horas, conforme criticidade do site) — valor contratual fixo, não muda durante a vigência (Consultor de Projetos, Vanessa).
- Se a Vivo quiser aumentar a potência instalada além do contratado, a Moura só fornece mediante solicitação formal de aumento (Técnico).

## 9. Governança operacional interna (quem faz o quê no contrato Vivo)

Mapa de responsabilidades reconstruído a partir de Andrea, Aline Souza e Josi:
- **José Espinosa**: gestão/operação do contrato no dia a dia — ponto de contato direto com a Vivo para questões operacionais e de campo.
- **Josiele (Josi)**: interface interna entre a fábrica (ACMO) e a Moura Energia — traduz demanda de instalação em programação de produção/estoque.
- **Daniel Garcia**: gestão financeira do contrato (faturamento, sinergia, furto, balanço) — "visão helicóptero", não mergulha no operacional.
- **Aline / Karina (Driele/Adriele como executiva de conta)**: relacionamento comercial, RFPs, negociação de preço e escopo.
- **Andrea (PO)**: modelagem de novos negócios/expansões do contrato (ex.: legado), orquestração entre áreas.
- **RSM**: braço de campo — instalação, comissionamento e manutenção (preventiva a cada 6 meses).
- Aponta-se **lentidão de SLA interno de resposta** como problema recorrente (Driele) — fluxo passa por muitas pessoas sem processo formalizado, gerando atrito com o cliente.

## 10. Evolução em curso do contrato/relação com a Vivo

- **Sites legados**: novo projeto em desenho (Driele, Josi, Andrea) para a Moura assumir sites **já existentes** da Vivo (hoje 90% dos sites contratados são novos, "Greenfield" do zero; só ~10% são "ampliação"; legado puro ainda não é atacado, José Espinosa estima ~30 mil sites da Vivo nessa condição, similar à TIM).
- Modelo em construção: Moura **compra o ativo legado do cliente e devolve como aluguel** ("sale and leaseback") — mencionado por Andrea, Josi e Espinosa como caminho mais provável.
- Passos do desenho: reuniões com engenharia da Vivo, vistorias de sites para avaliar estado de conservação, modelagem de negócio do zero (Driele, Andrea).
- Há também conversa para redimensionar bateria por site com base em consumo real (menos capacidade instalada de saída, complementando por demanda) — já testado em lote de 60 gabinetes (Josi, Espinosa).

## 11. Proposta de valor — como cada um verbaliza (para comparar discursos)

| Entrevistado | Como resume o valor |
|---|---|
| Thiago Mello | Tira limitação de CAPEX da operadora; Moura assume risco de furto/durabilidade; personalização futura por região |
| Driele | "Eu sou especialista no que eu faço e deixo você ser especialista no que você faz" |
| Consultor de Projetos | Diferencial está no "como" (execução), não no produto físico; granularidade e proatividade de dados frente ao "espelhamento pobre" que a operadora já tem |
| Josi | Cliente não precisa se preocupar; furto é a principal dor a resolver |
| Gustavo Moura | Servitização como resposta à perda de competitividade industrial; diversificação de receita e uso de vantagens do grupo (RSM, fábrica, capital) |
| Francisco (TI) | Futuro está em vender o "intangível" (dados), não só o gabinete físico |
| José Espinosa | Antecipar a dor do cliente, estar "dentro" dele; monetizar dados como "assinatura premium" no futuro |
| Daniel Garcia | Zero CAPEX, SLA de reposição muito mais rápido que compra tradicional, granularidade de monitoramento vs. sistemas "pobres" das operadoras, reciclagem/logística reversa |
| Aline Souza | "Faz o que você é bom e deixa a energia que a gente resolve"; foco forte em antifurto |
| Vanessa (ITEM) | Assumir telemetria e manutenção que a operadora fazia sozinha; robustez técnica como diferencial de longo prazo |
| Andrea (PO) | Backup contínuo + SLA + compliance regulatório + zero CAPEX + foco no core business; autocrítica de que hoje comunicam pouco do impacto financeiro amplo |

## 12. Autocrítica comum entre os entrevistados (padrão que se repete)

1. **Proposta de valor "pobre"/pouco quantificada** — quase ninguém consegue tangibilizar financeiramente o risco assumido pela Moura (Thiago Mello, Aline Souza, Andrea, Daniel Garcia).
2. **Dúvida se estão falando com as pessoas certas** dentro das operadoras (Thiago Mello, Andrea, Gustavo Moura).
3. **Medo de perda de emprego** por parte de quem opera hoje nas operadoras, como barreira recorrente em TIM e Claro (Driele, Josi, Aline Souza).
4. **Time comercial despreparado/com alta rotatividade** e sem material robusto de apresentação (Thiago Mello, José Espinosa, Aline Souza, Driele).
5. **Falta de processo/SLA interno formalizado**, gerando lentidão e atrito com o cliente (Driele, Aline Souza, Vanessa/Francisco no aspecto técnico).
6. **Maturidade do produto ainda baixa** frente ao roadmap original ("Moura Cube") — decisão estratégica pendente entre manter o básico ou investir em robustez (Vanessa, Francisco).
7. **Legado é a maior oportunidade não capturada** — hoje quase todo o contrato é sobre sites novos, não sobre o parque já instalado (Josi, José Espinosa, Daniel Garcia, Andrea, Driele).
