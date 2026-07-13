# Vanessa — ITEM (P&D) — Overview + Produto/Serviço

**Papel:** Coordenadora do time de P&D digital (hardware/software/firmware) e qualidade/homologação no ITEM, desde dez/2024. Duas conversas: uma breve institucional (Overview Moura + ITEM) e uma longa e técnica (Sobre o produto + serviço), onde ela conta a história completa do produto Telecom desde a origem.

---

## 1. Proposta de valor

**O que a Moura Energia entrega (Fato — o "insight" fundador do negócio, segundo o ITEM):** "as operadoras hoje têm muita dificuldade [...] têm furto [...] não conseguem fazer o monitoramento [...] a saúde dessa bateria para trocar tempo antes dela não conseguir dar carga e recair na multa. Então, por quê? Ao invés de só vender a bateria, a gente não vende o serviço."

**Problema que resolve (Fato):** telemetria/manutenção que a operadora fazia sozinha antes (com sistema próprio da fonte, para cumprir Anatel), agora feita pela Moura com mais informação e responsabilidade.

**Clientes (Fato):** TIM (primeiro piloto/POC), depois Telefônica.

**Valor percebido (Fato — quando perguntada diretamente):** "Da telemetria ser feita por nós e não mais pela operadora [...] A questão da manutenção também é bem importante [...] a gente ficando com o serviço, a gente é que vai lá resolver pra ela."

**Diferenciais (Fato — o que a Moura entrega além do que a operadora já tinha nativamente):** a fonte já manda dados para a nuvem própria da operadora (telemetria nativa, obrigatória para Anatel); "o que o nosso dá e o que o nosso a longo prazo [...] tem potencial de dar, cobre isso que as operadoras têm [e adiciona] mais informação e mais gatilhos e deveria prover mais segurança e confiabilidade do que só o espelhamento que eles têm."

**Interpretação:** Vanessa é a única entrevistada que consegue articular com precisão técnica *o que exatamente* a Moura entrega a mais do que a própria fonte/operadora já teria nativamente — dado essencial para qualquer discurso de valor mais rigoroso, mas que não aparece de forma tão clara nas falas do time comercial.

---

## 2. Desafios internos

### Na área dela (Tecnologia/Produto — ITEM)
- **Problema:** a POC "virou produto rápido demais". **Impacto:** produto foi a campo ainda experimental, sem a robustez planejada. **Quote:** "Isso não era produto. Isso ainda era experimental [...] a gente sabia que tinham fragilidades [...] a solução ia evoluir gradativamente" — mas isso não aconteceu no ritmo planejado: "começou a corrida com outro tempo. A gente de P&D tava tentando amadurecer o produto enquanto ele já tava sendo instalado."
- **Problema:** consumo de dados excessivo do modem comercial atual. **Impacto:** custo de OPEX elevado, ainda não capturado. **Quote:** "tem gabinete consumindo mais de 2 gigas" — teste do ITEM mostrou que a versão planejada consumiria ~15MB em 5 dias vs. ~300MB do modem atual.
- **Problema:** segurança física limitada (só cadeado Bluetooth). **Impacto:** módulo de segurança mais robusto (sensores de temperatura/vibração, trava reforçada) nunca foi desenvolvido. **Quote:** "hoje a gente tem um cabeado, que é da Promon [...] mas ele é só um cadeado [...] No máximo ele avisa assim, arrombou."
- **Problema:** divisão de responsabilidade de hardware não resolvida. **Impacto:** possível gargalo de tempo/prioridade. **Quote:** "o time não é grande e ele se divide, a gente perde e suporta [...] pode gerar um certo gargalo" — diferente do BES, já totalmente transferido para a Moura.
- **Problema:** perda de contato direto com o cliente final. **Impacto:** menos feedback direto de campo para o P&D. **Quote:** "vocês não têm mais acesso ao cliente final. Vocês têm que sempre pedir a engenharia pra intermediar."

### Percepção sobre desafios de outras áreas
- **Problema (processo/instalação):** falhas recorrentes de instalação. **Impacto:** causa raiz de boa parte dos incidentes de campo. **Quote:** "ainda hoje acontece [...] muitas falhas de processo, falhas de qualidade [...] verificar se o lugar tem ou não conexão. Na hora que o cara instala, ele conecta um cabo errado, usa um material errado." Exemplo concreto: site onde a bateria "descarregou completamente e o site morreu" porque nunca foi ligado à energia.
- **Problema (atribuição de causa):** ITEM é acionado por padrão mesmo quando o problema não é do Connect. **Impacto:** desperdício de esforço de investigação. **Quote:** "toda vez que gera uma dúvida, ah, é o Conect e falhou. Aí a gente é chamada e quando chega, não é o Conect."

---

## 3. Áreas internas

**Moura Energia / engenharia de novos negócios:**
- Papel: "o nosso cliente de fato é engenharia de novos negócios [...] é como se a gente fosse um terceirizado" — mesmo estando no mesmo grupo, a relação funcional é quase de prestação de serviço interno.

**Andréia (PO):**
- Papel: decide entre opções técnicas apresentadas pelo ITEM (ex.: se a fonte deve embarcar mais funcionalidades ou não) — "a gente vai oferecer opções pra Andréia. Ela vai escolher qual opção que quer."

**TI da Moura:**
- Papel: fez um espelhamento da plataforma do ITEM com outra identidade visual (plataforma MEX) a partir de requisitos vindos da Moura Energia — sem contato direto do ITEM com essa demanda: "a gente não teve esse contato direto."

**Pessoas internas-chave recomendadas por ela para aprofundamento:** João Machado (engenheiro técnico, desde a fundação — sabe causas raiz de falência de outras empresas do setor e riscos/gargalos) e Marcos Malveira (gerente do ITEM, visão de negócio/estratégia, desenhou a solução técnica com Thiago Mello).

---

## 4. Modelo comercial

*Não é foco dela*, mas contribui um dado histórico relevante:

**Como surgiu a primeira venda (Fato):** a POC/dispositivo criado pelo ITEM foi testado primeiro no site da **TIM** (não Telefônica) — "Fizemos isso aqui com a Tim, no site da Tim [...] Amor Energia, ela nasceu do item [...] o berço, de fato, foi aqui."

**Quem decidiu vender (Fato):** quando a POC "deu certo", a decisão veio de fora do ITEM — "aí disseram, vamos vender [...] quem viu o valor foi o cliente" (confirmado por ela).

*Não abordado: fluxo comercial atual, objeções, diferenças entre clientes.*

---

## 5. Visão sobre os clientes

**Comportamento/necessidades (Fato):** o que a plataforma ajuda a responder para quem opera (ex.: Espinosa) — saúde/estado dos sites, melhor momento de manutenção, garantia de autonomia contratual, alertas de degradação/furto indireto, análise geográfica cruzada com dados climáticos.

**Maturidade tecnológica do cliente (Fato):** a operadora já recebe telemetria nativa da fonte antes mesmo de contratar a Moura — "tem uma parte do gabinete que, por exemplo, a Tinha Viva, elas acessam livremente [...] Porque eles têm o sistema duplicado do nosso [...] Eles são obrigados a ter esse espelhamento."

**Interpretação:** essa fala é um dado crítico — a informação básica de telemetria **já existe** de forma nativa na operadora antes mesmo de contratar a Moura; a decisão de compra do cliente não pode se apoiar apenas em "ter monitoramento", e sim na qualidade/confiabilidade/proatividade adicional que a Moura promete entregar — algo ainda não plenamente maduro segundo a própria Vanessa.

---

## 6. Barreiras de expansão

- **Internas:** risco de escalabilidade ligado à maturidade do produto, não ao mercado — "pra gente, o único risco da escalabilidade hoje é pela maturidade do produto [...] Se a gente vai continuar como tá e fazer só o básico [...] Ou se a gente vai fazer o roadmap que foi pensado."
- **Mercado (histórico do setor como alerta):** "várias empresas [que tentaram] entrar nesse setor faliram [...] o sistema de monitoramento que hoje as operadoras têm[,] ele não consegue sanar esses gargalos [...] o custo do OPEX fica muito alto [...] o contrato é muito longo [...] você só vai gastando dinheiro para manter o sistema e ele começa a não trazer retorno."

**Interpretação:** ela é a única entrevistada que articula, de forma quase causal, por que outras empresas do setor fracassaram — e conecta isso diretamente ao risco que a própria Moura corre se não amadurecer o produto na velocidade necessária, antes de escalar mais.

---

## 7. Ecossistema e mercado

**Sobre o ITEM como instituição (Fato):** ICT (instituição de ciência e tecnologia) registrada no Ministério de Ciência e Tecnologia, sob o guarda-chuva Moura, sediada em Belo Jardim (com extensão em Recife); atua em P&D, fomento e inovação para toda a empresa, incluindo parcerias externas com outras ICTs e empresas do setor energético.

**Fornecedores (Fato):** dependência de decisão de fornecedor chinês para evoluir a fonte — precisa que ele aceite embarcar a solução, cobre preço absorvível, e depende de decisão estratégica da Moura sobre manter propriedade intelectual internamente ou delegar.

**Tendências (Fato):** já desenvolveram versões do sistema para aplicação bancária e data center, além de um projeto até 2027/2028 unindo telecom e BES no conceito de VPP (virtual power plant).

*Não abordado: concorrência nomeada, TowerCos, parceiros comerciais, integradores.*

---

## 8. Visão de futuro

**Próximos passos (Fato):** projeto para "amadurecer a solução e propor uma nova arquitetura" saindo do modelo atual (Raspberry Pi/dongle 4G comercial) para algo mais robusto — desafio de gerir a transição entre parque "legado" e novos sites.

**Novos modelos (Fato — "chassi único", convergente com a visão de Francisco/TI):** concentrar telecom + BES + futuro HomeBES numa mesma base de dados — "eu vou estar na casa de CPFs e CNPJs de pequeno porte [...] imagine a quantidade de informação."

**Riscos (Fato):** dependência de decisão de fornecedor chinês (ver seção 7).

**Prioridades (Fato — encerramento da entrevista):** "o único risco da escalabilidade hoje é pela maturidade do produto [...] se isso realmente é um diferencial do mercado ou não [...] para que realmente a solução, no longo prazo, se diferencie de qualquer outra. E ganhe naquela relação de CAPEX e OPEX."

---

## 9. Hipóteses para validação (Fase 2 — com operadoras)

| O que o time interno acredita (opinião de Vanessa) | Hipótese estruturada para testar com o mercado |
|---|---|
| O risco de escalabilidade é a maturidade do produto (não o mercado) — alarmes falsos, falta de módulo de segurança robusto. | O ceticismo comercial de TIM/Claro pode já estar ligado a **casos concretos de falha técnica que a operadora vivenciou** — testar diretamente com engenharia dessas operadoras se episódios específicos de instabilidade/alarme falso influenciaram a decisão de não avançar. |
| A operadora já tem telemetria nativa da fonte (para cumprir Anatel) antes mesmo de contratar a Moura. | O argumento comercial "nós damos monitoramento" pode não ser suficientemente diferenciado, já que o cliente já tem telemetria própria — testar diretamente com a engenharia da operadora **o que especificamente falta** no sistema nativo dela hoje. |
| Outras empresas do setor faliram porque o sistema de monitoramento não conseguia sanar os gargalos e o OPEX fugiu de controle. | As operadoras podem carregar **memória de fracassos anteriores** de fornecedores de servitização de energia, gerando ceticismo estrutural — testar se esse histórico é mencionado espontaneamente pelas operadoras e quais garantias mitigariam esse ceticismo. |

---

## 10. Pessoas-chave para falar dentro do cliente (operadora)

**Já conversados:** nenhum contato direto com cliente final (operadora) é relatado por ela.

**Fato explícito sobre a ausência de acesso:** "a gente já teve muito próximo [...] depois desse contato ficou assim, ó, vocês não têm mais acesso ao cliente final. Vocês têm que sempre pedir a engenharia pra intermediar."

**Interpretação:** essa é, em si, uma informação relevante para a Fase 2 — o ITEM (fonte primária do conhecimento técnico mais profundo do produto) está estruturalmente isolado do cliente final por uma política interna da própria Moura, o que significa que qualquer hipótese técnica levantada por ela nunca foi testada diretamente com quem usaria essa informação do lado da operadora.

---

## 11. Outros insights

- **Ela fornece a explicação mais completa de todo o conjunto de entrevistas sobre o histórico técnico do produto** (Moura Connect → Moura Lock/Moralonqui → insight de servitização → Moura Cube conceitual → POC/Connect Plus atual) — esse histórico deveria ancorar qualquer seção do report sobre evolução de produto.
- **A revelação de que a operadora já tem telemetria nativa da fonte** é, possivelmente, o achado técnico mais importante para revisar o discurso comercial atual — nenhum outro entrevistado do lado comercial demonstrou ter clareza dessa distinção, o que sugere um desalinhamento entre o que a tecnologia sabe e o que a venda comunica.
