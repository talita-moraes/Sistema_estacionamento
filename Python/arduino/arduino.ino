
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

int vez =0;
char usuariotipo = 'A'
 
void loop() {
  // put your main code here, to run repeatedly:
   if (vez != 1) {
    vez = 1;
    Serial.println(1); 
    Serial.println(2); 
   }
   
   if(Serial.available() > 0){

      byte verificar = Serial.read();
      char tipo = verificar;

      if(tipo == usuariotipo ){
        Serial.println(true);

        byte leitura = Serial.read();
        char mensagem = leitura;
        // exibir no display
        
       }else{
        Serial.println(false);
      }
    
  }
  
}

