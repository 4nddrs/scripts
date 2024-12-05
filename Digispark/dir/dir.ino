#include "DigiKeyboard.h"
#define kbd_es_es
bool executed = false; // Variable para controlar si el código se ha ejecutado

void setup() {
  // put your setup code here, to run once:
  DigiKeyboard.delay(5000); // Espera 5 segundos antes de comenzar
}

void loop() {
  // Verifica si el código ya se ha ejecutado
  if (!executed) {
    DigiKeyboard.update();
    DigiKeyboard.sendKeyStroke(0);
    DigiKeyboard.delay(1000);
    DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT); //run
    DigiKeyboard.delay(500);
    DigiKeyboard.println("cmd");
    DigiKeyboard.delay(1000);
    DigiKeyboard.println("color a");
    DigiKeyboard.delay(500);
    DigiKeyboard.println("dir/s");
    DigiKeyboard.sendKeyStroke(KEY_F11);

    executed = true; // Marca que el código ya se ha ejecutado
  }
}
