# Francisco — Diretor de TI (Moura)

**Papel:** Diretor de TI do grupo Moura, envolvido desde a concepção do projeto de servitização em 2022.

## Origem do projeto (visão de TI)
- Início por volta de 2022: discussões sobre novos modelos de negócio, coincidindo com aproximação da Moura com a AWS (que tem metodologia própria de inovação, "working backwards").
- Um dia de imersão na sede da AWS em São Paulo reuniu: Francisco (tecnologia), Marcos Malveira (do ITEM, P&D), Ana Beatriz Rocha (negócio), Tiago Mello e Danilo Campedo (comercial, não está mais na empresa) — saíram com um "present lease" (backlog) do que apresentar ao mercado.
- Em paralelo, o comercial já vinha conversando com a TIM para os pilotos/POC.
- Formou-se o time de produto "Energia como Serviço" (MEX) para tocar o MVP, com a filosofia de "montar um Lego" (usar peças existentes) em vez de construir tudo do zero.
- Três pilares definidos desde o início: hardware (na estação), firmware (controle) e software (camada de gestão/cliente).
- Já se sabia que os maiores desafios seriam telecomunicação (conectividade) e furto (grande dor das operadoras).
- Naquela época havia ~15 sites; hoje (na data da entrevista) são mais de 400.

## Papel atual da TI
- TI reorganizada há 2 anos em 4 Business Units (distribuição, manufatura, Moura Participações, "outros negócios" — onde está o Energia como Serviço), saindo de uma lógica de projetos para produtos.
- Maior desafio hoje: extrair o máximo do hardware/software/firmware que foi concebido de forma preliminar e evoluiu rápido — "processo ainda de aprendizagem".

## Problema central identificado: instalação, não conectividade
- O maior "vilão" da alarmística não é primariamente telecomunicação, mas sim **erros de instalação** do hardware/firmware em campo (a fonte, componente central de coleta de dados, foi instalada incorretamente em muitos sites).
- Estimativa dele: cerca de **70-80 sites** (na época, ~30-35% dos sites) com esse tipo de problema detectado.
- Vanessa (ITEM) já havia compartilhado com a equipe MJV um compilado de erros de campo (fio errado, energia não ligada, porta errada instalada).
- Aponta falha de "handover"/departamentalização: TI, ITEM (P&D) e engenharia não estão suficientemente integrados; falta uma governança de priorização mais forte por parte da Andrea (PO).

## O que a plataforma entrega hoje / deveria entregar
1. Alarmística preditiva de furto (idealmente detectar o ato, não só constatar depois).
2. Ação proativa antes de falha (visita preventiva, cumprir SLA contratual).
3. Informações para a própria operadora sobre uso de recursos, oscilação de energia, tickets do mês — não é obrigatório fornecer, mas visto como diferencial monetizável no futuro.
- Hoje só entregam **relatórios** para a operadora — ela não tem acesso direto à plataforma.
- Quem acessa a plataforma: time de operação da Moura Energia (inclui NOC, com um terceiro envolvido), gestão de ativos, RSM.

## Valor gerado pelos dados
- Para a Moura (fábrica): entender ciclos de carga/descarga, dimensionar corretamente capacidade de bateria por tipo de site — um "teste em grande escala" que pode alimentar produtos futuros.
- Para a Moura Energia: quanto mais eficiente e preditiva a operação (menos visitas de campo), maior a rentabilidade; também menciona otimização de spare parts e da própria RSM.
- Vê o cadeado/controle de acesso físico como um ponto de fragilidade — hoje terceirizado (empresa externa fornece o sistema de trava Bluetooth), o que preocupa do ponto de vista de segurança da informação (falta de redundância, risco se o terceiro for comprometido).

## Motivos de o crescimento não ser mais acelerado
1. Falta de confiabilidade 100% do ecossistema (eventos ainda acontecendo).
2. Alto CAPEX por gabinete/instalação — precisa de eficiência de instalação para começar a amortizar.
3. Falta de disciplina e padrões estabelecidos de instalação/checagem.
- Ritmo hoje: ~100 instalações por mês, cerca de 80% do que é liberado pela operadora (que libera de forma cadenciada via sistema próprio).

## Evolução da plataforma (v2)
- Trabalhando em uma nova arquitetura para suportar volume de dados maior (duplicar/triplicar).
- Duas frentes: plataforma PSI (software) e nova versão do "Connect" (hoje um Raspberry Pi rodando em campo) — ainda não atingiu uma versão de hardware "estável nível industrial".
- ITEM deveria estabilizar e entregar produto final para a engenharia assumir evolução contínua — hoje isso ainda não aconteceu integralmente ("estabilizando" é a palavra mais adequada, segundo ele).
- Roadmap H2 (2-3 anos): VPP (virtual power plant) — bateria com inteligência para descarregar/carregar de forma otimizada, aproveitando energia solar.
- H3: hidrogênio (visão de outro entrevistado presente, não a dele) — ele não tem visibilidade dessa fronteira para o produto específico de telecom.

## Riscos e composição de fornecedores
- Preocupação relevante (mencionada como "tira meu sono"): dependência de componentes chineses sem padrão de segurança da informação estabelecido, sem monitoramento contínuo 24x7 formalizado para os produtos já em operação.
- Para telecom, o custo de uma solução de segurança robusta é desafiador porque o ticket mensal (FII) é pequeno frente ao CAPEX inicial alto — "a gente tem que ser criativo".

## Visão de futuro / benchmarks
- Referências: EUA (qualidade, especialmente Califórnia — clima parecido com o Brasil), China (velocidade, mas qualidade inferior — não deveria ser modelo pra Moura), Israel (cybersecurity), Palo Alto e Fortinet (segurança), Oracle (processamento de dados), WEG (ousadia estratégica, "risco muito mais alto" que a Moura assume).
- Vê o futuro do negócio em **vender o intangível** (dados) — analogia com Amazon/Magazine Luiza migrando de varejo para tecnologia — e em usar a infraestrutura física instalada (sites) para gerar outras receitas (ex.: eletroposto, dados agregados, outros sensores).
- Sugestão de "chassi único": concentrar telecom + BES + HomeBES numa mesma base de dados/plataforma para ganhar densidade de informação.
- Diferencial a explorar: em vez de discurso só de custo, mostrar tempo de reestabelecimento em caso de roubo/queda e penalidades regulatórias da Anatel evitadas.
