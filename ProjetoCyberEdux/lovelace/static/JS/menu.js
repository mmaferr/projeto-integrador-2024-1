function toggleContent(unidade_id) {
    fetch(`/get_unidade_content/${unidade_id}/`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("titulo-conteudo").textContent = data.titulo;
            document.getElementById("texto-conteudo").textContent = data.texto;
            document.getElementById("imagem-conteudo").src = data.imagem_url;
        })
        .catch(error => console.error('Erro ao obter conteúdo da unidade:', error));
}