Fisierul de configurare poate sa inceapa cu linii goale, eventual linii comentate prin precedarea acesteia cu <!--
Exista 4 sectiunii ale fisierului:
-States
-Sigma
-Gama
-Delta

sectiunea States este anticipata prin cuvantul "States:", netinand cont daca literele sunt de tipar sau nu. Analog si celelalte sectiuni sunt precedate in felul acesta. "---Start---" si "---End---" semnifica inceputul si sfarsitul sectiunii respective. Comentarii pot aparea intre linii. De asemenea sectiunile pot aparea in orice ordine. Pentru States, avem starile ca grupare de litere cu cifre dupa. Pentru sigma si gama, caracterele pot fi orice, mai putin ',' si simboluri speciale. Delta este reprezentata in forma q1, a -> q2, b, L/R, unde q1 reprezinta starea curenta, 'a', litera celulei pe care capul masinii turing se afla, q2, starea in care inanteaza capul, 'b', litera care e scrisa in celula in care a fost 'a' si L/R pentru schimbarea capului masinii turing in stanga sau dreapta.