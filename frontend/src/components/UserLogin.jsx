import axios from 'axios';
import React from 'react';
import { Form, Button } from 'react-bootstrap';
import {Container} from 'react-bootstrap';
import App from '../App';
import { render } from 'react-dom';




function AuthLogin() {
  function enviarRequisicao(event) {
    event.preventDefault(); // Evita o comportamento padrão de envio do formulário
  
    const form = event.target;
    const csrfToken = form._csrf.value; // Obtenha o valor do CSRF token do campo oculto
  
    // Configurando o cabeçalho da requisição com o token CSRF
    const headers = {
      'X-CSRFToken': csrfToken
    };
  
    // Extrair os dados do formulário
    const formData = new FormData(form);
  
    // Fazendo a requisição com o cabeçalho configurado
    axios.post('http://127.0.0.1:8000/api/auth-user/', formData, { headers })
      .then(response => {
        console.log(response)
        alert("Autenticado Com Sucesso!")
      })
      .catch(error => {
        // Manipular erros da requisição
      });
  }

  const csrfToken = window.csrfToken; // Certifique-se de que csrfToken esteja definido
  return (
    <>
    <Container className='bg-light rounded box-register '>
          <Form onSubmit={enviarRequisicao} method='POST' action='http://127.0.0.1:8000/api/auth-user/'>
          <Form.Group className="mb-3" controlId="formBasicUsername">
            <Form.Control name="_csrf" type="hidden" defaultValue={csrfToken} />
          </Form.Group>

          <Form.Group className="mb-3" controlId="formBasicUsername">
            <Form.Label>Username</Form.Label>
            <Form.Control name="username" type="text" placeholder="Username" />
          </Form.Group>

          <Form.Group className="mb-3" controlId="formBasicPassword">
            <Form.Label>Password</Form.Label>
            <Form.Control name="password" type="password" placeholder="Password" />
          </Form.Group>

          <Button variant="primary" type="submit">
            Submit
          </Button>
          
        </Form>
    </Container>
    </>
  );
}

export default AuthLogin;
