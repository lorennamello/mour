# Vanessa — ITEM (P&D) — Overview + Produto/Serviço

**Papel:** Coordenadora do time de P&D digital (hardware, software, firmware) e de qualidade/homologação no ITEM (Instituto de Tecnologia da Moura), desde dezembro/2024. Formada em computação, background em sistemas embarcados/IoT. O ITEM é uma ICT (instituição de ciência e tecnologia) registrada no Ministério de Ciência e Tecnologia, sob o guarda-chuva Moura, sediada em Belo Jardim (com extensão em Recife). O produto Telecom **nasceu no ITEM**.

## O que é o ITEM
- Atua em P&D, fomento e inovação para toda a Moura — presta suporte a outras engenharias (fábrica, novos negócios/Telecom e BES, outros produtos como a bicicleta elétrica "Ela").
- Faz parcerias com outras ICTs e empresas do setor energético/transformação digital.
- Coordenações: digital (hardware/software/firmware), qualidade (QA, homologação, normatização), e BES (armazenamento de energia).
- Também atua em eletrificação veicular.

## Linha do tempo do produto Telecom (histórico técnico detalhado)
1. **Moura Connect** (bateria para empilhadeiras): dispositivo acoplado à bateria para monitorar remotamente se o uso estava dentro da garantia — primeira tentativa de transformação digital do produto bateria.
2. **Moura Lock/"Moralonqui"** (contexto telecom): dispositivo de trava com foco em reduzir furto — evoluiu para trava eletromecânica que aumentava o esforço necessário para arrancar a bateria, com comunicação em nuvem. Não avançou por complexidade de adaptação ao modelo de gabinete (e outras razões). Nessa fase ainda **não existia o CNPJ Moura Energia**.
3. **Insight do ITEM**: em vez de só vender a bateria, vender o **serviço** — tirar a responsabilidade de monitoramento/manutenção da operadora e assumir via digital.
4. **Moura Cube** (conceito mais completo, não implementado por completo): incluiria telemetria, segurança e novos sensoriamentos (ex.: contagem de "UIs" — unidades/slots vazios do gabinete — para saber remotamente se há espaço para outra operadora entrar; conectividade não só 4G, mas satelital/link dedicado).
5. **POC/piloto real com a TIM**: usaram uma placa já conhecida, modem 4G comercial (inicialmente chip Claro, depois multi-operadora), conectado à fonte, para provar o conceito e gerar dashboard próprio. Essa POC "deu certo" e **virou produto rapidamente** — mesmo sendo, segundo ela, ainda experimental, sem a robustez planejada originalmente (Moura Cube).

## Por que a Moura viu valor na POC
- Assumir a telemetria e a responsabilidade de avisar sobre problemas em vez da operadora ter que olhar para isso.
- Assumir a manutenção: se a bateria cair, romper, ser furtada ou perder comunicação, a Moura (via RSM) resolve — a operadora não precisa acionar ninguém.

## Problemas herdados dessa "corrida" entre maturação e escala
- **Consumo de dados excessivo**: modem comercial usado hoje consome de forma "grosseira" (chegando a >2GB por gabinete); em teste controlado do ITEM, a versão planejada (modem integrado) consumiria ~15MB em 5 dias vs. ~300MB do modem atual — grande diferencial de custo de OPEX não capturado ainda.
- **Segurança física limitada**: hoje só existe um cadeado Bluetooth (fornecido por parceiro, "Promon") que no máximo avisa que foi aberto — não há trava reforçada nem sensores adicionais (temperatura para detectar maçarico, vibração) que dificultariam e detectariam furto mais rápido, como planejado originalmente.
- **Divisão de responsabilidade "confusa"**: ITEM ainda dá suporte de **hardware** (inclusive investigação de causas de falha) porque a transferência tecnológica de hardware para a Moura ainda não aconteceu (diferente do BES, que já foi totalmente transferido). O ITEM também mantém a base de dados/backend do software, enquanto a Moura (via plataforma espelhada "MEX") cuida do front-end/dashboard.
- Esse suporte dividido é apontado como um possível "gargalo" (time pequeno do ITEM dividido entre P&D novo e suporte legado).

## Nomenclatura / evolução da plataforma
- Antes MAS (Moura as a Service) → depois **MEX** (Moura Energia como Serviço) quando virou empresa. Nome "Moraes a Service" foi trocado por recomendação de consultoria de marca (Silvio Meira/TDS) por soar mal.
- Plataforma do ITEM (mais completa/técnica) e a plataforma MEX (espelhamento com identidade visual e requisitos solicitados pela Moura Energia) coexistem.
- Moura Energia conectou outros sistemas à base (ex.: GLPI para tickets).

## Sobre o Connect Plus (produto físico atual)
- Parceria com a **Esfera Labs** para o encapsulamento/case.
- Internamente: um Raspberry Pi rodando a programação própria; conecta-se à fonte via cabeamento; envia dados para a nuvem AWS via modem multi-operadora ("dongle" — hoje ainda chip Claro na prática, apesar do multi-operadora "Minify").
- Multi-operadora não resolve regiões sem sinal de nenhuma operadora — daí a ideia original de contemplar NB-IoT, satélite ou link dedicado.
- Cada fornecedor/modelo de gabinete e fonte precisa passar por um processo de "homologação" no ITEM — traduzir o protocolo de comunicação da fonte para o formato do dispositivo Moura. Às vezes é simples, às vezes é um projeto de P&D inteiro (protocolos não documentados/não nacionais). Fornecedores homologados hoje: **Delta** (não fornece mais) e **NRSys**; em processo de homologação com **ZTE** e outros.

## CAPEX x OPEX — tensão estrutural do produto
- A POC virou produto rápido demais e "setou" um CAPEX enxuto; mas a ideia original era que uma solução mais robusta reduzisse o OPEX no médio/longo prazo — hoje esse equilíbrio ainda não foi atingido.
- Ela atribui a falência de outras empresas do setor a esse mesmo padrão: sistema de monitoramento incapaz de sanar os gargalos (furto, multa Anatel, degradação de ativos, custo de troca de bateria), OPEX foge de controle em contratos muito longos, setor "degrada" a empresa.

## O que a plataforma entrega (perspectiva de quem está em campo, ex.: Espinosa)
- Saúde/estado dos sites: quando fazer manutenção, se a autonomia contratual está garantida.
- Autonomia calculada como variável central.
- Alertas de degradação, furto (indireto, não direto — não existe ainda o "módulo de segurança" robusto planejado), falha de comunicação.
- Análise geográfica/cruzamento com dados climáticos.
- Consumo elétrico: corrente, temperatura, tensão de barra, estado de carga.

## Quem acessa e quem entrega o quê à operadora
- A operadora (Vivo, TIM) hoje tem acesso ao "espelhamento próprio" que a fonte já gera para cumprir a Anatel — isso já existia **antes** do Moura Energia.
- O diferencial do sistema Moura é dar **mais informação, mais gatilhos e mais confiabilidade** do que esse espelhamento nativo da fonte — e assumir a responsabilidade da manutenção, que a operadora não precisa mais fazer.
- ITEM não tem mais contato direto com o cliente final (operadora) — precisa sempre passar pela engenharia de "novos negócios" da Moura, que intermedeia (regra criada depois que tiveram contato direto no passado).

## Fluxo ponta a ponta do processo de implantação
- Comprado (ex.: da China) → chega na Unidade 10 (comissionamento/montagem) → vai para a RSM → instala → a partir daí RSM cuida da manutenção.
- Já há tentativa de pré-análise de conectividade da região **antes** de aceitar contrato/site (para não se comprometer com um site sem 4G).
- Reconhece falhas de processo recorrentes: gabinete instalado mas não ligado à energia (caso relatado: bateria descarregou 100% e o site "morreu" por erro de instalação, não por falta de manutenção).
- Quando ocorre falha, muitas vezes é atribuída ao "Connect" (ITEM é chamado), mas na investigação frequentemente não é o Connect — reforça a necessidade de melhor diagnóstico de causa raiz e evolução de processo, não só de produto.

## Risco de escalabilidade (síntese dela)
- O único risco real de escalar hoje é a **maturidade do produto** — decisão estratégica pendente: continuar fazendo "só o básico" ou seguir o roadmap original (robustez que diferenciaria de qualquer concorrente na relação CAPEX/OPEX no longo prazo).
