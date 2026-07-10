# Consultor de Projetos da Moura Energia — Operação Vivo

**Papel:** Consultor de projetos na Moura Energia desde setembro/2025, responsável por monitorar/gerenciar os produtos implantados de Telecom e BES (operação pós-implantação). ~12 anos de casa Moura, passou por 4 áreas diferentes (estagiário de engenharia em Belo Jardim, RH/GPM como analista/supervisor de infraestrutura, gestor de projeto/produção na fábrica de baterias de lítio, e agora Moura Energia).

## Escopo da função
- Cuida do ativo depois que sai de "implantação" e entra em "operação" (quando a Vivo aceita o gabinete).
- Plano de manutenção preventiva a cada 6 meses, articulada com as RSMs.
- Manutenção corretiva: mapeia, acompanha e diagnostica alarmes/problemas/furtos e aciona o time de campo.
- Monitora dados de operação da plataforma; hoje a capacidade preditiva ainda é baixa.
- Se descreve como "guardião da plataforma" — a área de operações é quem mais usa a ferramenta no dia a dia.
- Também é "guardião" do processo de troubleshooting (N1 = NOC, N2 = pode ser ele, engenharia ou TI, N3 = outro nível) e da governança de mudanças de processo (existe um documento "MANHA" como padrão).

## Processo de implantação → operação
- Vivo nomeia o site ("o site XXX é seu"); time de implantação da Moura instala o gabinete.
- Fica uma "porta" disponível para a Vivo instalar seus próprios equipamentos; enquanto isso não acontece, um alarme pode surgir por problema de instalação que **não é responsabilidade da operação** (é pendência de implantação).
- A operação só assume plenamente depois que a Vivo confirma que instalou os equipamentos dela sem pendências — o aceite da operação se baseia no aceite da Vivo.

## Maior dor: vandalismo/furto
- Cerca de **7% dos gabinetes** já foram vandalizados (índice considerado alto e incômodo).
- O modelo de negócio foi baseado num percentual de referência de **2%** — ou seja, estão ~5 pontos percentuais acima do ideal.
- A Vivo reconhece que isso é normal do dia a dia deles ("vivo isso 4-5 vezes por dia").
- Mitigação em andamento: reforço da estrutura mecânica, estudo de rastreamento de bateria roubada, redimensionamento de energia (colocar menos bateria) para reduzir atratividade.

## Segunda dor: conectividade/confiabilidade de dados
- Alertas da plataforma têm "falsos positivos" (ex.: "porta aberta" sem porta ter sido aberta) e "falsos negativos" (não alerta quando algo de fato aconteceu).
- Isso gera retrabalho ou atraso na informação — às vezes ele só descobre um furto porque o **cliente liga avisando**, e a plataforma não mostra nada.
- Não sabe a causa raiz da não confiabilidade (só conhece a consequência).

## Sobre a plataforma
- Plataforma tem ~6 meses de vida (começou em janeiro); ainda "tem um caminho longo".
- O que falta: informação de **autonomia do site** (quantas horas de backup restam) não vem "vomitada" na tela — precisa ser garimpada; essa é a informação mais crítica pois é a que gera risco contratual/multa.
- Informação de acessos também não está como gostaria.
- O que já entrega bem: status online/offline em tempo real (ex.: de 412 sites, sabe quantos estão offline), permite refutar ou confirmar reclamações da Vivo sobre telemetria, consumo de dados por site vs. franquia contratada, status do cadeado (aberto/fechado), histórico documental do site (aba "projetos").
- Cálculo de autonomia: a plataforma mostra consumo em ampere dos equipamentos da Vivo; ele calcula a quantidade de bateria necessária para cobrir o DEC contratado (2, 3 ou 4 horas — valor contratual fixo por site).

## Relação com a Vivo
- Percepção como "muito positiva/colaborativa" — quando mostram print/evidência da telemetria, gera confiança ("esses caras sabem do que estão falando").
- Elogios recebidos: tempo de resposta, prontidão, cordialidade, decisões baseadas em fatos e dados.
- Relação dele é operacional, não estratégica.
- Maior preocupação da Vivo: **tempo de resposta / SLA de atendimento**. Exemplo: em Minas Gerais, a base da RSM está longe (ex.: Uberlândia fica a 6-7h da base), mas o contrato exige atendimento em até 4h em alguns casos.
- SLAs contratuais: 4h (mais crítico), 6h (médio), 12h (mais leve) — a confirmar com o contrato. Vivo costuma ser flexível na prática, mas o contrato "debaixo do braço" diria outra coisa.
- Considera os SLAs de atendimento uma "fraqueza" real da operação.

## RSM (Rede de Serviços Moura)
- É do Grupo Moura, mas outro CNPJ, com autonomia para terceirizar/subcontratar parceiros regionais.
- Sugeriu à RSM Minas Gerais que buscasse parceiros locais (quarteirização) após reclamação da Vivo.
- Mesmo problema se repete no BES (ex.: RSM Pernambuco atendendo o Pará).
- RSM Pernambuco atende também Rio Grande do Norte, Paraíba e Alagoas — ironicamente fica a "um quarteirão" do escritório onde a entrevista ocorreu, mas para Mossoró (interior do RN) o deslocamento é de ~12h de carro.

## Proposta de valor / diferencial (visão dele)
- O produto físico (gabinete) é o mesmo há 20 anos — a especificação é do próprio cliente, não há diferencial de produto ali.
- O diferencial está no **"como"**: qualidade de execução, comunicação proativa (dão status sem o cliente pedir), velocidade e forma de resolver os mesmos problemas que a operadora sempre teve.
- Cita que a operadora tem ~100 mil alarmes e prioriza atender só uma fração (~10%) por recurso limitado — a Moura, ao assumir, consegue cuidar de tudo com mais qualidade e dados.
- Concorrentes normalmente não têm sistema de monitoramento algum — quando acionados, "não contestam, simplesmente vão lá resolver gastando dinheiro". A Moura contesta com dados e, segundo ele, em ~90% dos acionamentos da Vivo o problema não era da Moura.

## Visão de futuro / potencial da plataforma
- Vê grande potencial de a plataforma agregar valor ao cliente final, mas ainda não encontraram a "flechada certa" — a informação vendida precisa ser algo que o cliente realmente não conseguiria obter sozinho.
- Personalização por cliente: entender a dor específica de cada operadora para moldar a oferta de dados.
