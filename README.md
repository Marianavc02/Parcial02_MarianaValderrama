# Parcial02_MarianaValderrama
<p>
Este proyecto es un microservicio desarrollado en Flask que recibe un número por la URL 
y devuelve una respuesta en formato JSON con los siguientes datos:
</p>

<ul>
  <li>El número recibido</li>
  <li>Su factorial</li>
  <li>Una etiqueta que indica si el <strong>número es par o impar</strong></li>
  <li>Un campo <code>"status": "ok"</code> que confirma que la solicitud fue procesada correctamente</li>
</ul>

<hr>

<h2> Como ejecutar el proyecto</h2>

<ol>
  <li><strong>Clonar el repositorio</strong></li>
  <pre><code>git clone https://github.com/Marianavc02/Parcial02_MarianaValderrama.git
cd Parcial02_MarianaValderrama</code></pre>

  <li><strong>Instalar dependencias</strong></li>
  <pre><code> pip install -r requirements.txt</code></pre>
  <li><strong>Ejecutar App</strong></li>
  <pre><code>python app.py</code></pre>

   <li><strong>Abre en el navegador</strong></li>
  <pre><code>http://127.0.0.1:5000</code></pre>


  <li><strong>Probar en el navegador con url (ejemplo)</strong></li>
  <pre><code>http://127.0.0.1:5000/numero/5</code></pre>

  <p><strong>Respuesta esperada:</strong></p>
  <pre><code>{
  "etiqueta": "impar",
  "factorial": 120,
  "numero_recibido": 5,
  "status": "ok"
}</code></pre>
</ol>


<h2>(respuesta de parcial)</h2>
<p>
Si el microservicio necesitara comunicarse con otro que guarde los resultados en una base de datos,
lo que haria seria que luego de calcular el factorial y enviaria el dato del resultado , el numero,
y su etiqueta para que sean almacenados en unabase de datos 
Para hacerlo debo crear la URL del otro servicio mediante una variable de entorno y enviarle los datos mediante una petición HTTP.
asi uno se encarga solo del cálculo y el otro gestiona el historial y ambos trabajan de forma autónoma,
  cumpliendo así con los principios de una arquitectura de microservicios.
</p>



