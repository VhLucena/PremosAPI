import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import json

## Just to mock
def ReadInputJSON(filename):
    with open("/Users/viniciuslucena/Google Drive/0s Projetos/PGII/PremosAPI/input/input.json") as json_file:
        input = json.load(json_file)
        return input
## ----------------------------------------

def CreateLabelEncoding():
    encodingMapping = dict()
    
    encodingMapping['Nao'] = 0
    encodingMapping['Sim'] = 1
        
    encodingMapping['Ausente'] = 0
    encodingMapping['Presente'] = 1
    
    encodingMapping['Leve'] = 0
    encodingMapping['Grave'] = 1
    
    encodingMapping['Nenhum'] = 0
    encodingMapping['De 1 a 5 anos'] = 1
    encodingMapping['De 6 a 12 anos'] = 2
    encodingMapping['De 13 a 25 anos'] = 3
    encodingMapping['Mais de 25 anos'] = 4

    encodingMapping['Nao casado'] = 0
    encodingMapping['Casado'] = 0
    
    encodingMapping['Ens.Fundamental'] = 1
    encodingMapping['Ens.Medio ou Superior'] = 2
    
    encodingMapping['Nao conta com ninguem'] = 0
    encodingMapping['Conta com 1'] = 1
    encodingMapping['Conta com 2'] = 2
    encodingMapping['Conta com 3'] = 3
    encodingMapping['Conta com 4'] = 4
    
    return encodingMapping

def CreateTemplate():
    template = {}
    
    template['g08_Feminino'] = np.nan
    template['g08_Masculino'] = np.nan
    template['hiv_Nao fez ou nao sabe'] = np.nan
    template['hiv_Nao reagente'] = np.nan
    template['hiv_Reagente'] = np.nan
    template['d17_Nao'] = np.nan
    template['d17_Nao bebe ha 6 meses'] = np.nan
    template['d17_Sim'] = np.nan
    template['p11_a_Nao'] = np.nan
    template['p11_a_Sim'] = np.nan
    template['p11_a_Sim mas somente sob efeito de droga ou em abstinencia'] = np.nan
    template['G10_cor_pele_Branco'] = np.nan
    template['G10_cor_pele_Negro'] = np.nan
    template['G10_cor_pele_Pardo e outros'] = np.nan
    template['E10_emprego_Nao trabalha'] = np.nan
    template['E10_emprego_Trabalho Irregular'] = np.nan
    template['E10_emprego_Trabalho Regular'] = np.nan
    template['M_doencas_Apenas 1'] = np.nan
    template['M_doencas_Duas ou mais'] = np.nan
    template['M_doencas_Nenhuma'] = np.nan
    template['F8ABC_1 destes é dependente'] = np.nan
    template['F8ABC_2 ou 3 destes são dependentes'] = np.nan
    template['F8ABC_Parceiro, amigos e família não são dependentes'] = np.nan
    template['abuso_sexual_crack_Antes do crack'] = np.nan
    template['abuso_sexual_crack_Junto ou depois do crack'] = np.nan
    template['abuso_sexual_crack_Nao'] = np.nan
    template['m10'] = np.nan
    template['m11'] = np.nan
    template['e36'] = np.nan
    template['d20'] = np.nan
    template['count_drogas'] = np.nan
    template['d42'] = np.nan
    template['d45'] = np.nan
    template['l2'] = np.nan
    template['F2_dic'] = np.nan
    template['f16'] = np.nan
    template['f21'] = np.nan
    template['P1_dic'] = np.nan
    template['P13_14A'] = np.nan
    template['G12_conjugal'] = np.nan
    template['E1_escolaridade'] = np.nan
    template['F9ABC'] = np.nan
    template['g09_idade'] = np.nan
    template['d11'] = np.nan
    template['F40_dic'] = np.nan
    template['d03'] = np.nan
    template['D8_9'] = np.nan
    template['porc_vida_doente'] = np.nan
    template['D25B_div_idade'] = np.nan
    template['D27B_div_idade'] = np.nan
    template['D28B_div_idade'] = np.nan
    template['D57_div_idade'] = np.nan
    template['CTQ_PN_dic1'] = np.nan
    template['CTQ_PA_dic1'] = np.nan
    template['CTQ_EN_dic1'] = np.nan
    template['CTQ_EA_dic1'] = np.nan
    template['CTQ_SA_dic1'] = np.nan
    template['abuso_sexual_vida'] = np.nan
    template['abuso_sexual_infancia'] = np.nan
    template['abuso_fisico_vida'] = np.nan
    template['abuso_fisico_infancia'] = np.nan
    template['scid_f_tept'] = np.nan
    template['scid_f_tco'] = np.nan
    template['scid_psicoticos_dic'] = np.nan
    template['scid_depressao_dic'] = np.nan
    template['scid_bipolar_dic'] = np.nan
    template['scid_alcool_dic'] = np.nan
    template['scid_alimentar_dic'] = np.nan
    template['scid_ansiedade_outros_dic'] = np.nan
    template['ctq_pos_sum'] = np.nan
    
    index = ['g08_Feminino', 'g08_Masculino', 'hiv_Nao fez ou nao sabe', 'hiv_Nao reagente', 'hiv_Reagente', 'd17_Nao', 'd17_Nao bebe ha 6 meses', 'd17_Sim', 'p11_a_Nao', 'p11_a_Sim', 'p11_a_Sim mas somente sob efeito de droga ou em abstinencia', 'G10_cor_pele_Branco', 'G10_cor_pele_Negro', 'G10_cor_pele_Pardo e outros', 'E10_emprego_Nao trabalha', 'E10_emprego_Trabalho Irregular', 'E10_emprego_Trabalho Regular', 'M_doencas_Apenas 1', 'M_doencas_Duas ou mais', 'M_doencas_Nenhuma', 'F8ABC_1 destes é dependente', 'F8ABC_2 ou 3 destes são dependentes', 'F8ABC_Parceiro, amigos e família não são dependentes', 'abuso_sexual_crack_Antes do crack', 'abuso_sexual_crack_Junto ou depois do crack', 'abuso_sexual_crack_Nao', 'm10', 'm11', 'e36', 'd20', 'count_drogas', 'd42', 'd45', 'l2', 'F2_dic', 'f16', 'f21', 'P1_dic', 'P13_14A', 'G12_conjugal', 'E1_escolaridade', 'F9ABC', 'g09_idade', 'd11', 'F40_dic', 'd03', 'D8_9', 'porc_vida_doente', 'D25B_div_idade', 'D27B_div_idade', 'D28B_div_idade', 'D57_div_idade', 'CTQ_PN_dic1', 'CTQ_PA_dic1', 'CTQ_EN_dic1', 'CTQ_EA_dic1', 'CTQ_SA_dic1', 'abuso_sexual_vida', 'abuso_sexual_infancia', 'abuso_fisico_vida', 'abuso_fisico_infancia', 'scid_f_tept', 'scid_f_tco', 'scid_psicoticos_dic', 'scid_depressao_dic', 'scid_bipolar_dic', 'scid_alcool_dic', 'scid_alimentar_dic', 'scid_ansiedade_outros_dic', 'ctq_pos_sum']      
    return pd.Series(data=template, index=index)

def CreateOneHot(input_file, original_input):
    # g08
    genero = original_input['input']['g08']
    if(genero == 'Masculino'):
        input_file['g08_Masculino'] = 1
        input_file['g08_Feminino'] = 0
    else:
        input_file['g08_Masculino'] = 0
        input_file['g08_Feminino'] = 1
    # ---------------------------------------------------------------        
    # hiv
    hiv = original_input['input']['hiv']
    if(hiv == 'Reagente'):
        input_file['hiv_Reagente'] = 1
        input_file['hiv_Nao fez ou nao sabe'] = 0
        input_file['hiv_Nao reagente'] = 0
        
    elif (hiv == 'Nao fez ou nao sabe'):
        input_file['hiv_Reagente'] = 0
        input_file['hiv_Nao fez ou nao sabe'] = 1
        input_file['hiv_Nao reagente'] = 0
    
    else:
        input_file['hiv_Reagente'] = 0
        input_file['hiv_Nao fez ou nao sabe'] = 0
        input_file['hiv_Nao reagente'] = 1
    # ---------------------------------------------------------------
    # d17 
    abstinencia_alcool = original_input['input']['d17']
    
    if(abstinencia_alcool == 'Sim'):
        input_file['d17_Sim'] = 1
        input_file['d17_Nao'] = 0
        input_file['d17_Nao bebe ha 6 meses'] = 0
    elif(abstinencia_alcool == 'Nao'):
        input_file['d17_Sim'] = 0
        input_file['d17_Nao'] = 1
        input_file['d17_Nao bebe ha 6 meses'] = 0
    elif(abstinencia_alcool ==  'Nao bebe ha 6 meses'):
        input_file['d17_Sim'] = 0
        input_file['d17_Nao'] = 0
        input_file['d17_Nao bebe ha 6 meses'] = 1
    # ---------------------------------------------------------------        
    # p11_a
    alucinacoes = original_input['input']['p11_a']
    
    if(alucinacoes == 'Sim'):
        input_file['p11_a_Sim'] = 1
        input_file['p11_a_Nao'] = 0
        input_file['p11_a_Sim mas somente sob efeito de droga ou em abstinencia'] = 0
    elif(alucinacoes == 'Nao'):
        input_file['p11_a_Sim'] = 0
        input_file['p11_a_Nao'] = 1
        input_file['p11_a_Sim mas somente sob efeito de droga ou em abstinencia'] = 0
    elif(alucinacoes ==  'Sim mas somente sob efeito de droga ou em abstinencia'):
        input_file['p11_a_Sim'] = 0
        input_file['p11_a_Nao'] = 0
        input_file['p11_a_Sim mas somente sob efeito de droga ou em abstinencia'] = 1
    # ---------------------------------------------------------------
    # G10_cor_pele
    cor_pele = original_input['input']['G10_cor_pele']
    
    if(cor_pele == 'Branco'):
        input_file['G10_cor_pele_Branco'] = 1
        input_file['G10_cor_pele_Negro'] = 0
        input_file['G10_cor_pele_Pardo e outros'] = 0
    elif(cor_pele == 'Negro'):
        input_file['G10_cor_pele_Branco'] = 0
        input_file['G10_cor_pele_Negro'] = 1
        input_file['G10_cor_pele_Pardo e outros'] = 0
    elif(cor_pele ==  'Pardo e outros'):
        input_file['G10_cor_pele_Branco'] = 0
        input_file['G10_cor_pele_Negro'] = 0
        input_file['G10_cor_pele_Pardo e outros'] = 1
    # ---------------------------------------------------------------
    # E10_emprego
    emprego = original_input['input']['E10_emprego']
    
    if(emprego == 'Nao trabalha'):
        input_file['E10_emprego_Nao trabalha'] = 1
        input_file['E10_emprego_Trabalho Irregular'] = 0
        input_file['E10_emprego_Trabalho Regular'] = 0
    elif(emprego == 'Trabalho Irregular'):
        input_file['E10_emprego_Nao trabalha'] = 0
        input_file['E10_emprego_Trabalho Irregular'] = 1
        input_file['E10_emprego_Trabalho Regular'] = 0
    elif(emprego ==  'Trabalho Regular'):
        input_file['E10_emprego_Nao trabalha'] = 0
        input_file['E10_emprego_Trabalho Irregular'] = 0
        input_file['E10_emprego_Trabalho Regular'] = 1
    # ---------------------------------------------------------------
    # M_doencas
    doencas = original_input['input']['M_doencas']
    
    if(doencas == 'Apenas 1'):
        input_file['M_doencas_Apenas 1'] = 1
        input_file['M_doencas_Duas ou mais'] = 0
        input_file['M_doencas_Nenhuma'] = 0
    elif(doencas == 'Duas ou mais'):
        input_file['M_doencas_Apenas 1'] = 0
        input_file['M_doencas_Duas ou mais'] = 1
        input_file['M_doencas_Nenhuma'] = 0
    elif(doencas ==  'Nenhuma'):
        input_file['M_doencas_Apenas 1'] = 0
        input_file['M_doencas_Duas ou mais'] = 0
        input_file['M_doencas_Nenhuma'] = 1
    # ---------------------------------------------------------------
    # F8ABC
    problema_drogas = original_input['input']['F8ABC']
    
    if(problema_drogas == '1 destes é dependente'):
        input_file['F8ABC_1 destes é dependente'] = 1
        input_file['F8ABC_2 ou 3 destes são dependentes'] = 0
        input_file['F8ABC_Parceiro, amigos e família não são dependentes'] = 0
    elif(problema_drogas == '2 ou 3 destes são dependentes'):
        input_file['F8ABC_1 destes é dependente'] = 0
        input_file['F8ABC_2 ou 3 destes são dependentes'] = 1
        input_file['F8ABC_Parceiro, amigos e família não são dependentes'] = 0
    elif(problema_drogas ==  'Parceiro, amigos e família não são dependentes'):
        input_file['F8ABC_1 destes é dependente'] = 0
        input_file['F8ABC_2 ou 3 destes são dependentes'] = 0
        input_file['F8ABC_Parceiro, amigos e família não são dependentes'] = 1
    # ---------------------------------------------------------------
    # abuso_sexual_crack
    abuso_sexual_crack = original_input['input']['abuso_sexual_crack']
    
    if(abuso_sexual_crack == 'Antes do crack'):
        input_file['abuso_sexual_crack_Antes do crack'] = 1
        input_file['abuso_sexual_crack_Junto ou depois do crack'] = 0
        input_file['abuso_sexual_crack_Nao'] = 0
    elif(abuso_sexual_crack == 'Junto ou depois do crack'):
        input_file['abuso_sexual_crack_Antes do crack'] = 0
        input_file['abuso_sexual_crack_Junto ou depois do crack'] = 1
        input_file['abuso_sexual_crack_Nao'] = 0
    elif(abuso_sexual_crack ==  'Nao'):
        input_file['abuso_sexual_crack_Antes do crack'] = 0
        input_file['abuso_sexual_crack_Junto ou depois do crack'] = 0
        input_file['abuso_sexual_crack_Nao'] = 1
    # ---------------------------------------------------------------
    return input_file

def HandleNumericAttributes(input_file, original_input):
    list_of_attr = ['count_drogas', 'g09_idade', 'd11', 'd03', 'porc_vida_doente', 'D25B_div_idade', 'D27B_div_idade', 'D28B_div_idade', 'D57_div_idade', 'ctq_pos_sum']
    
    for attr in list_of_attr:
        input_file[attr] = original_input['input'][attr]
    return input_file

def Encoding(input_file):
    original_input = input_file
    input_file = input_file['input']
    input_file.drop('algorithm', axis=0, inplace=True)
    
    encodingMapping = CreateLabelEncoding()
    template = CreateTemplate()
    
    for key,value in input_file.items():
        if value in encodingMapping and key in template:
            template[key] = encodingMapping[value]

    template = CreateOneHot(template, original_input)
    
    template = HandleNumericAttributes(template, original_input)

    return template.as_matrix().reshape([1,70])

if __name__ == "__main__":
        inputFile = ReadInputJSON('input.json')
        inputFile = pd.DataFrame.from_dict(inputFile)
        inputFile = Encoding(inputFile['input'])

        from sklearn.tree import DecisionTreeClassifier
        clf = DecisionTreeClassifier()
        df_train = pd.read_csv('/Users/viniciuslucena/Google Drive/0s Projetos/PGII/Database/402_TreinoDatabase.csv')
        df_test = pd.read_csv('/Users/viniciuslucena/Google Drive/0s Projetos/PGII/Database/402_TesteDatabase.csv')
        X_train = df_train.iloc[:,:-1]
        y_train = df_train.iloc[:,-1]

        X_test = df_train.iloc[:,:-1]
        y_test = df_test.iloc[:,-1]

        clf.fit(X_train, y_train)

        predicted = clf.predict(inputFile)
        print()





































































































































































































