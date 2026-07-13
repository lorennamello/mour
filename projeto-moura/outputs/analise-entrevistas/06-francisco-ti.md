# Francisco — Diretor de TI (Moura)

**Papel:** Diretor de TI do grupo Moura, envolvido desde a concepção do projeto em 2022 (aproximação com AWS).

---

## 1. Proposta de valor

**O que a Moura Energia entrega (Fato):** recursos de alarmística — "a capacidade preditiva de saber quando o site está sendo furtado [...] agir proativamente [...] fornecer informações para a própria operadora [...] é um diferencial para o negócio."

**Problema que resolve (Fato):** hoje, defensivamente (furto, SLA); no futuro, monetização de dados como produto em si.

**Clientes (Fato):** operadoras de telecom em geral, com foco atual na Vivo/Telefônica.

**Valor percebido (Fato):** dados coletados ajudam a própria Moura (fábrica) a entender ciclos de bateria, dimensionar capacidade corretamente, identificar falhas de qualidade — "para a Moura, para a fábrica" isso é "extremamente positivo", mesmo antes de qualquer benefício repassado ao cliente.

**Diferenciais (Fato — visão de futuro):** "o futuro [...] é a gente conseguir vender aquilo que é intangível [...] os dados [...] têm algum valor. O que a gente não descobriu ainda [...] é como interpretar esses [dados]." Cita analogia com Amazon/Magazine Luiza (migração de varejo para tecnologia).

**Interpretação:** Francisco enxerga o valor do produto em duas camadas temporais distintas: hoje é operacional/defensivo; no futuro, monetização de dados como produto em si — ele é o único entrevistado que articula essa segunda camada como tese central de sua visão.

---

## 2. Desafios internos

### Na área dele (Tecnologia)
- **Problema:** causa raiz dos problemas de alarmística não é primariamente conectividade, mas erro de instalação de hardware/firmware em campo. **Impacto:** ~70-80 sites afetados (~30-35% na época). **Quote:** "quando a gente vai investigando [...] a gente vê que não é telecomunicação puramente [...] existe uma questão ainda fundamental [...] que é a parte de como foi feita a instalação do hardware e do firmware."
- **Problema:** plataforma ainda em fase de maturação de hardware. **Impacto:** "essa versão final estável nunca chegou, em termos de hardware [...] no patamar industrial" — o "Connect" roda numa Raspberry Pi não industrializada.
- **Problema:** dependência de terceiro para controle de acesso (cadeado Bluetooth). **Impacto:** fragilidade de segurança da informação. **Quote:** "hoje a gente tem terceirizado e é muito sensível [...] eu dependo do terceiro estar totalmente funcional [...] ainda é uma fragilidade do ecossistema."
- **Problema:** ausência de padrão de segurança da informação com fornecedores chineses. **Impacto:** risco não mitigado. **Quote:** "tem me preocupado muito, tirado meu sono [...] alguns componentes chineses que a gente tem usado [...] a gente não tem [...] um monitoramento contínuo, 24 por 7."

### Percepção sobre desafios de outras áreas
- **Problema:** falha de handover entre TI, ITEM e engenharia. **Impacto:** atraso na resolução de problemas conhecidos. **Quote:** "teve, na minha visão, uma deficiência no handover de algumas questões [...] a gestão de priorização de André[a]" deveria orquestrar melhor essas frentes.

---

## 3. Áreas internas

**ITEM:**
- Papel: entregou a POC original, ainda dá suporte de **hardware** e mantém a base de dados de telecom.
- Dependência: a Moura "conseguiu absorver em parte o software, mas ela usa ainda por trás a base de dados que a gente [ITEM] suporta" — diferente do BES, já transferido tecnologicamente.
- Lacuna: essa divisão de responsabilidade não está resolvida — cria potencial gargalo de tempo e prioridade.

**Andrea (PO):**
- Papel esperado: orquestradora da priorização entre TI, ITEM e engenharia.
- Lacuna: "é o que a gente vem, entre aspas, costurando" — sugere que essa costura ainda não é fluida.

**Moura Energia (como "cliente interno"):**
- Papel: aciona TI/ITEM via engenharia de novos negócios.
- Dependência/conflito: "a Moura Energia [...] acaba alocando micro[times] nas outras empresas da Moura para servir a ela [...] o pagamento para a gente vem de forma indireta [...] é como se a gente fosse um terceirizado", mesmo estando no mesmo grupo.

---

## 4. Modelo comercial

*Não é a área dele*, mas contribui uma leitura de possível "moeda de troca" comercial: parceria de conectividade (satélite/link dedicado) com operadoras em transição para tecnologia (ex.: TIM/V8) poderia se somar ao contrato de energia — ideia ainda especulativa, não testada comercialmente.

*Não abordado: como surgem oportunidades hoje, objeções específicas, diferenças entre clientes.*

---

## 5. Visão sobre os clientes

**Comportamento/tendência (Fato — via conversa recente com a V8/TIM):** "o plano do cara é o seguinte [...] Enquanto telecomunicação, eu não tenho como me sustentar a operação [...] Eu preciso partir para [...] fazer tecnologia [...] É tanto que a Claro se juntou com a HITS, a [TIM] comprou a V8 e a Vivo está patinando ainda nesse meio de campo."

**Necessidades emergentes (Fato — projeto Anel Verde, SP):** operadoras avançando para "soluções compostas" de infraestrutura + tecnologia (ex.: visão computacional substituindo cabines de pedágio).

**Interpretação:** ele antecipa que as operadoras vão precisar cada vez mais de parceiros como a Moura à medida que migram para "tecnologia" além do core de telecom — isso posicionaria a Moura não como fornecedora de energia, mas como parte de um ecossistema de infraestrutura mais amplo.

---

## 6. Barreiras de expansão

- **Internas (ele enumera 3 motivos explicitamente):** (1) falta de confiabilidade 100% do ecossistema; (2) CAPEX alto de gabinete/instalação exigindo eficiência para começar a amortizar; (3) falta de disciplina/padrões de instalação e checagem — "a gente ainda não aprendeu a trabalhar de forma disciplinar."
- **Mercado/Clientes:** ritmo de expansão também depende do cliente ("ela direciona [...] tem esse lote aqui disponível"), mas ele julga esse fator menos relevante que os 3 internos.
- **Externas:** tensão estrutural CAPEX x OPEX — "para telecom, o FII é muito pequeno mensal [...] é muito grande[,] o CAPEX inicial [...] mas o FII mensal não comporta a solução [de segurança robusta 24x7]. A gente tem que ser criativo."

---

## 7. Ecossistema e mercado

**Telecom / tendências (Fato):** operadoras migrando para "soluções compostas" (TIM/V8, Claro/HITS); Vivo "patinando" nesse movimento.

**Concorrência / benchmarks internacionais (Fato):** EUA (qualidade, especialmente Califórnia — clima parecido com o Brasil), China (velocidade mas qualidade inferior — "a China deixa de ser uma inspiração nessa perspectiva de qualidade"), Israel (cybersecurity), Palo Alto e Fortinet (segurança), Oracle (processamento de dados a médio prazo).

**Benchmark nacional:** WEG — "eles são muito mais ousados [...] o risco é muito mais alto [...] a gente aqui na Amor sempre vai ser um passo de cada vez."

**Fornecedores (Fato):** dependência de componentes chineses, com tensão entre discurso crítico e prática — "eles copiam tudo [...] se não fosse [as barreiras tarifárias], eu não sei o que seria da indústria nacional" — mesmo assim, a Moura acabou de assinar contrato com fornecedor chinês (K-12) para nova linha na metalúrgica.

**Posicionamento da Moura Energia (Interpretação):** headroom para se tornar parceira de infraestrutura ampliada (não só energia) das operadoras, aproveitando a tendência delas de buscar parceiros de "tecnologia".

---

## 8. Visão de futuro

**Evolução do serviço (Fato — dois eixos):**
1. **Dados** — infraestrutura de hardware/software para suportar crescimento, armazenar e processar mais dados, "transformar isso em informação".
2. **Ampliar a receita além do FII mensal** — usar a capacidade física instalada (sites) para outras finalidades: carregamento veicular ("eletroposto"), sensores adicionais (meteorologia, temperatura), replicar o modelo para outros setores (bancos, home base).

**Novos modelos (Fato):** conceito de "chassi único" — unificar telecom + BES + HomeBES numa mesma base/infraestrutura de dados.

**Longo prazo (Fato):** roadmap H1/H2/H3 mencionado (dele e de outro participante presente) — H2 é aproximadamente o horizonte do VPP (fotovoltaico + BES); H3 seria hidrogênio, mas ele reconhece não ter visibilidade dessa fronteira aplicada especificamente a telecom.

**Prioridades (Fato):** recomendação de discurso — migrar o argumento de custo puro para argumento de **nível de serviço regulatório** (tempo de reestabelecimento após furto, penalidade Anatel evitada) como gatilho mais forte de decisão do que economia direta.

---

## 9. Hipóteses para validação (Fase 2 — com operadoras)

| O que o time interno acredita (opinião de Francisco) | Hipótese estruturada para testar com o mercado |
|---|---|
| Raiz dos problemas de confiabilidade da plataforma é erro de instalação, não conectividade. | O cliente pode estar atribuindo instabilidade **à tecnologia da Moura como um todo**, quando a causa concreta é erro de instalação em sites específicos — testar se casos pontuais de falha já pesaram na decisão de não expandir o contrato, e se isolar a causa muda a percepção. |
| Operadoras estão migrando para "soluções compostas" (tecnologia + infraestrutura). | As operadoras podem estar abertas a uma parceria de infraestrutura mais ampla com a Moura, desde que a oferta inclua também **conectividade** — testar apetite por esse tipo de parceria com a área de tecnologia/inovação das operadoras, não apenas com engenharia de energia. |
| Argumento de custo puro é fraco; nível de serviço regulatório (Anatel) seria gatilho mais forte. | Ainda não testado por ninguém internamente — confirmar diretamente com compliance/regulatório das operadoras se o risco de multa Anatel realmente pesa na decisão, ou se as multas são raras/pouco relevantes no orçamento delas. |

---

## 10. Pessoas-chave para falar dentro do cliente (operadora)

**Já conversados, segundo ele:**
- Contato recente com a **V8** (empresa de tecnologia comprada pela TIM) — não é conversa tradicional com "cliente operadora", mas usada para entender tendência estratégica do grupo TIM.

**Não conversados / lacuna identificada:**
- Não nomeia contatos específicos em Vivo, TIM ou Claro — foco mais em tendência de mercado do que em relacionamento.
- Sugere, sem nomear, que o interlocutor-chave futuro poderia ser a área de **tecnologia/inovação** das operadoras, e não a engenharia de infraestrutura tradicional.

---

## 11. Outros insights

- **Tensão entre discurso e prática sobre fornecedores chineses:** ele é crítico da dependência da China por risco de segurança/propriedade intelectual, mas reconhece que a própria Moura acabou de assinar contrato com fornecedor chinês — vale monitorar esse ponto no report como um risco de governança ainda não resolvido, não apenas retórico.
- **Ele é o único entrevistado que trata "vender dados" como o verdadeiro produto final de longo prazo**, mais do que energia em si — essa visão, se validada, mudaria a forma como o report deveria enquadrar a proposta de valor de longo prazo da Moura Energia (de "fornecedora de backup" para "empresa de dados de infraestrutura").
