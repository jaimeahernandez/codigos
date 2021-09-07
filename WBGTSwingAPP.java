/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author usuario
 */
public class WBGTSwingAPP extends javax.swing.JFrame {

    /**
     * Creates new form WBGTSwingAPP
     */
    public WBGTSwingAPP() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        TXTHUMEDA = new javax.swing.JTextField();
        TXTGLOBO = new javax.swing.JTextField();
        TXTSECA = new javax.swing.JTextField();
        TXTCTERMICA = new javax.swing.JTextField();
        jScrollPane1 = new javax.swing.JScrollPane();
        TXTRESULTADOS = new javax.swing.JTextArea();
        BTCALCULAR = new javax.swing.JButton();
        BTLIMPIAR = new javax.swing.JButton();
        jLabel6 = new javax.swing.JLabel();
        TXTLA = new javax.swing.JTextField();
        jLabel7 = new javax.swing.JLabel();
        TXTLP = new javax.swing.JTextField();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Calculo del Indice WBGT");
        setName("Calculo del Indice WBGT"); // NOI18N

        jLabel1.setFont(new java.awt.Font("Tahoma", 1, 18)); // NOI18N
        jLabel1.setText("CALCULO INDICE WBGT");

        jLabel2.setText("TH (°C): ");

        jLabel3.setText("TG (°C):");

        jLabel4.setText("TS (°C):");

        jLabel5.setText("CT (Kcal/H):");

        TXTRESULTADOS.setColumns(20);
        TXTRESULTADOS.setRows(5);
        jScrollPane1.setViewportView(TXTRESULTADOS);

        BTCALCULAR.setText("CALCULAR");
        BTCALCULAR.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BTCALCULARActionPerformed(evt);
            }
        });

        BTLIMPIAR.setText("LIMPIAR");
        BTLIMPIAR.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                BTLIMPIARActionPerformed(evt);
            }
        });

        jLabel6.setText("LA:");

        TXTLA.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                TXTLAActionPerformed(evt);
            }
        });

        jLabel7.setText("LP:");

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(28, 28, 28)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jScrollPane1)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addGroup(layout.createSequentialGroup()
                                        .addGap(90, 90, 90)
                                        .addComponent(jLabel1))
                                    .addGroup(layout.createSequentialGroup()
                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                                            .addGroup(javax.swing.GroupLayout.Alignment.LEADING, layout.createSequentialGroup()
                                                .addComponent(jLabel5)
                                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                                .addComponent(TXTCTERMICA, javax.swing.GroupLayout.PREFERRED_SIZE, 51, javax.swing.GroupLayout.PREFERRED_SIZE)
                                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                                .addComponent(jLabel6, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                                            .addGroup(layout.createSequentialGroup()
                                                .addComponent(jLabel2)
                                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                                .addComponent(TXTHUMEDA, javax.swing.GroupLayout.PREFERRED_SIZE, 51, javax.swing.GroupLayout.PREFERRED_SIZE)
                                                .addGap(18, 18, 18)
                                                .addComponent(jLabel3)))
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                            .addComponent(TXTGLOBO, javax.swing.GroupLayout.DEFAULT_SIZE, 71, Short.MAX_VALUE)
                                            .addComponent(TXTLA))
                                        .addGap(18, 18, 18)
                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                            .addGroup(layout.createSequentialGroup()
                                                .addComponent(jLabel4)
                                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                                .addComponent(TXTSECA, javax.swing.GroupLayout.PREFERRED_SIZE, 53, javax.swing.GroupLayout.PREFERRED_SIZE))
                                            .addGroup(layout.createSequentialGroup()
                                                .addComponent(jLabel7)
                                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                                .addComponent(TXTLP)))))
                                .addGap(0, 15, Short.MAX_VALUE))))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(124, 124, 124)
                        .addComponent(BTCALCULAR)
                        .addGap(29, 29, 29)
                        .addComponent(BTLIMPIAR)))
                .addGap(34, 34, 34))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jLabel1)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 31, Short.MAX_VALUE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel2)
                    .addComponent(jLabel3)
                    .addComponent(TXTHUMEDA, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(TXTGLOBO, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel4)
                    .addComponent(TXTSECA, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel5)
                    .addComponent(TXTCTERMICA, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel6)
                    .addComponent(TXTLA, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel7)
                    .addComponent(TXTLP, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(BTCALCULAR)
                    .addComponent(BTLIMPIAR))
                .addGap(18, 18, 18)
                .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(17, 17, 17))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void BTCALCULARActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BTCALCULARActionPerformed
        //ENTRADAS
        double TH=Double.parseDouble(TXTHUMEDA.getText());
        double TG=Double.parseDouble(TXTGLOBO.getText());
        double TS=Double.parseDouble(TXTSECA.getText());
        double CT=Double.parseDouble(TXTCTERMICA.getText());
        double LA=Double.parseDouble(TXTLA.getText());
        double LP=Double.parseDouble(TXTLP.getText());
                  
        //PROCESO
        double indiceWBGT=(TH*0.7)+(TG*0.2)+(TS*0.1);
        
        //SALIDA
        TXTRESULTADOS.setText("RESULTADOS");
        TXTRESULTADOS.append("\n El indice WBGT es: "+indiceWBGT);
        if (indiceWBGT<LA){
            TXTRESULTADOS.append("\n El riesgo es BAJO");
        }else if (indiceWBGT>=LA && indiceWBGT<LP){
            TXTRESULTADOS.append("\n El riesgo es MEDIO");
        }else{
            TXTRESULTADOS.append("\n El riesgo es ALTO");
        }
        TXTRESULTADOS.append("\n La Carga Térmica es: "+CT);
        if (CT<200){
            TXTRESULTADOS.append(" LIVIANO");
        }else if (CT>=200 && CT<300){
            TXTRESULTADOS.append(" MODERADO");
        }else if (CT>=300 && CT<400){
            TXTRESULTADOS.append(" CLASIFICADO:PESADO");
        }else{
            TXTRESULTADOS.append(" CLASIFICADO:MUY PESADO");
        }
    }//GEN-LAST:event_BTCALCULARActionPerformed

    private void BTLIMPIARActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_BTLIMPIARActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_BTLIMPIARActionPerformed

    private void TXTLAActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_TXTLAActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_TXTLAActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(WBGTSwingAPP.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(WBGTSwingAPP.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(WBGTSwingAPP.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(WBGTSwingAPP.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new WBGTSwingAPP().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton BTCALCULAR;
    private javax.swing.JButton BTLIMPIAR;
    private javax.swing.JTextField TXTCTERMICA;
    private javax.swing.JTextField TXTGLOBO;
    private javax.swing.JTextField TXTHUMEDA;
    private javax.swing.JTextField TXTLA;
    private javax.swing.JTextField TXTLP;
    private javax.swing.JTextArea TXTRESULTADOS;
    private javax.swing.JTextField TXTSECA;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JScrollPane jScrollPane1;
    // End of variables declaration//GEN-END:variables
}