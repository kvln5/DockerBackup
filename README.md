Enunciado:
A aplicação BICA, precisa de ter backups configurados antes de ser colocada em produção. Esta aplicação é constituída por um backend e por uma base de dados Postgres. Toda a persistência e dados a salvaguardar estão na base de dados. O nosso desafio é implementar uma solução para efetuar backup à base de dados. Para tal, temos disponível um servidor Linux em que garantimos haver comunicação com a base de dados.

Requisitos
Criação de script de backup (a linguagem é indiferente, recomendamos Bash ou Python).
Este script deve executar dentro de um container Docker (todos os packages necessários a execução de containers, já se encontram instalados) no nosso servidor Linux.
Os backups devem ficar persistidos no disco local do nosso servidor Linux na diretoria /mnt/backups (que existe e tem permissões de leitura e escrita)
Queremos ter backups duas vezes ao dia, pelas 03:00 AM e pelas 14:00 PM (UTC)
No final da execução do script, o nosso backup deverá ser um ficheiro único de arquivo (zip/tgz/etc...) e que deverá ter como prefixo a data e hora da realização do backup, p.e. “bica-backup-2024-05-25_0300.tar.gz”
Queremos ter uma retenção de backups de X dias, onde X é o número de dias e que pode ser variável. Todos os backups anteriores a X dias, deverão ser apagados na execução das 03:00AM.
Os parâmetros de acesso à base de dados, deverão ser variáveis:
ip/host
porto
user
password
nome_da_db
Em caso de restart ou manutenção do nosso servidor Linux, o processo de backup deverá ser capaz de voltar a executar no próximo horário de backup sem intervenção adicional.
Idealmente os backups encontram-se encriptados.
Pretendemos com este exercício obter a documentação da solução, que entre outros, deverá conter:

Script de backup
Ficheiros relevantes à criação do container Docker, caso existam, como p.e. Dockerfile, Entrypoint, etc...
Ficheiros, configurações ou comandos utilizados que permitem a execução do backup, p.e.:
“docker run ...”
docker compose
crontab
scripts auxiliares
Identificação de outras variáveis utilizadas no script.
Packages adicionais necessários instalar no servidor.
