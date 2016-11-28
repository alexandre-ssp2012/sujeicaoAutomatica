import json

class ObrigacaoJson:

    dataSP = '''
            {
                "chave" : "obrigacaoAcessoria_1399301985605",
                "nome" : "SP - ECF (Cupom Fiscal) - Emissor de Cupom Fiscal",
                "criteriosVencimento" : [
                     {
                        "chave" : "criterio_1",
                        "descricao" : "Fabricante, o importador, a empresa distribuidora ou revendedora de equipamento ECF (relação de todos os equipamentos ECF comercializados no mês anterior independete do local de destino do equipamento)",
                        "aplicaveis" : [
                            {
                            "chave" : "aplicabilidade_1_1",
                            "descricao" : "Obriga - Fabricante, importador, empresa distribuidora ou revendedora de equipamento ECF"
                            }
                        ]
                     },
                     {
                        "chave" : "criterio_2",
                        "descricao" : "Usuário de ECF (relação dos equipamentos ECF movimentados)",
                        "aplicaveis" : [
                            {
                                "chave" : "aplicabilidade_2_1",
                                "descricao" : "Obriga - Estabelecimento que efetue operação com mercadoria ou prestação de serviços em que o destinatário ou o tomador do serviço seja pessoa física ou jurídica não-contribuinte do imposto."
                            },
                            {
                                "chave" : "aplicabilidade_2_2",
                                "descricao" : "Obriga - Estabelecimento com expectativa de receita bruta anual superior a R$ 120.000,00 (cento e vinte mil reais) deverá adotar Equipamento Emissor de Cupom Fiscal - ECF com memória de Fita-Detalhe (MFD)."
                            },
                            {
                                "chave" : "aplicabilidade_2_3",
                                "descricao" : "Obriga - Estabelecimento usuário de ECF que promover a saída interna ou interestadual de ECF novo ou usado."
                            }
                        ]
                     },
                     {
                        "chave" : "criterio_3",
                        "descricao" : "Usuário de ECF (conteúdo da leitura da Memória Fiscal)",
                        "aplicaveis" : [
                            {
                                "chave" : "aplicabilidade_3_1",
                                "descricao" : "Obriga - Estabelecimento que efetue operação com mercadoria ou prestação de serviços em que o destinatário ou o tomador do serviço seja pessoa física ou jurídica não-contribuinte do imposto."
                            },
                            {
                                "chave" : "aplicabilidade_3_2",
                                "descricao" : "Obriga - Estabelecimento com expectativa de receita bruta anual superior a R$ 120.000,00 (cento e vinte mil reais) deverá adotar Equipamento Emissor de Cupom Fiscal - ECF com memória de Fita-Detalhe (MFD)."
                            },
                            {
                                "chave" : "aplicabilidade_3_3",
                                "descricao" : "Obriga - Estabelecimento usuário de ECF que promover a saída interna ou interestadual de ECF novo ou usado."
                            }
                        ]
                     }
                ]
            }
           '''

    listaCriterioKey_1 = ["fabricante", "importador", "distribuidora", "revendedora", "equipamento ECF"]
    dictCriterioValue_1 = {"chaveObrigacao" : "obrigacaoAcessoria_1399301985605", "chaveCriterio" : "criterio_1", "descricao" : "Fabricante, o importador, a empresa distribuidora ou revendedora de equipamento ECF (relação de todos os equipamentos ECF comercializados no mês anterior independete do local de destino do equipamento)"}
    listaAplicabilidade_1 = ["fabricante", "importador", "distribuidora", "revendedora", "equipamento ECF"]
    dictAplicabilidade_1 = {"chaveObrigacao" : "obrigacaoAcessoria_1399301985605", "chaveAplicabilidade" : "aplicabilidade_1", "descricao": "Obriga - Fabricante, importador, empresa distribuidora ou revendedora de equipamento ECF"}

    listaCriterioKey_2 = ["ECF", "relação dos equipamentos ECF movimentados"]
    dictCriterioValue_2 = {"chaveObrigacao": "obrigacaoAcessoria_1399301985605",
                           "chaveCriterio": "criterio_2",
                           "descricao" : "Usuário de ECF (relação dos equipamentos ECF movimentados)"}
    listaAplicabilidade_2_1 = ["mercadoria", "prestação de serviços", "pessoa física", "pessoa jurídica", "não-contribuinte"]
    dictAplicabilidade_2_1 = {"chaveObrigacao": "obrigacaoAcessoria_1399301985605",
                            "chaveAplicabilidade": "aplicabilidade_2_1",
                            "descricao": "Obriga - Estabelecimento que efetue operação com mercadoria ou prestação de serviços em que o destinatário ou o tomador do serviço seja pessoa física ou jurídica não-contribuinte do imposto."}
    listaAplicabilidade_2_2 = ["receita > R$ 120.000,00"]
    dictAplicabilidade_2_2 = {"chaveObrigacao": "obrigacaoAcessoria_1399301985605",
                              "chaveAplicabilidade": "aplicabilidade_2_2",
                              "descricao": "Obriga - Estabelecimento com expectativa de receita bruta anual superior a R$ 120.000,00 (cento e vinte mil reais) deverá adotar Equipamento Emissor de Cupom Fiscal - ECF com memória de Fita-Detalhe (MFD)."}
    listaAplicabilidade_2_3 = ["ECF", "saída interna", "saída interestadual", "novo", "usado"]
    dictAplicabilidade_2_3 = {"chaveObrigacao": "obrigacaoAcessoria_1399301985605",
                              "chaveAplicabilidade": "aplicabilidade_2_3",
                              "descricao": "Obriga - Estabelecimento usuário de ECF que promover a saída interna ou interestadual de ECF novo ou usado."}

    listaCriterioKey_3 = ["ECF", "conteúdo da leitura da Memória Fiscal"]
    dictCriterioValue_3 = {"chaveObrigacao": "obrigacaoAcessoria_1399301985605", "chaveCriterio": "criterio_3", "descricao" : "Usuário de ECF (conteúdo da leitura da Memória Fiscal)"}
    listaAplicabilidade_3_1 = ["mercadoria", "prestação de serviços", "pessoa física", "pessoa jurídica", "não-contribuinte"]
    dictAplicabilidade_3_1 = {"chaveObrigacao": "obrigacaoAcessoria_1399301985605",
                              "chaveAplicabilidade": "aplicabilidade_3_1",
                              "descricao": "Obriga - Estabelecimento que efetue operação com mercadoria ou prestação de serviços em que o destinatário ou o tomador do serviço seja pessoa física ou jurídica não-contribuinte do imposto."}
    listaAplicabilidade_3_2 = ["receita > R$ 120.000,00"]
    dictAplicabilidade_3_2 = {"chaveObrigacao": "obrigacaoAcessoria_1399301985605",
                              "chaveAplicabilidade": "aplicabilidade_3_2",
                              "descricao": "Obriga - Estabelecimento com expectativa de receita bruta anual superior a R$ 120.000,00 (cento e vinte mil reais) deverá adotar Equipamento Emissor de Cupom Fiscal - ECF com memória de Fita-Detalhe (MFD)."}
    listaAplicabilidade_3_3 = ["ECF", "saída interna", "saída interestadual", "novo", "usado"]
    dictAplicabilidade_3_3 = {"chaveObrigacao": "obrigacaoAcessoria_1399301985605",
                              "chaveAplicabilidade": "aplicabilidade_3_3",
                              "descricao": "Obriga - Estabelecimento usuário de ECF que promover a saída interna ou interestadual de ECF novo ou usado."}

    def printJson(self):
        #data = self.data
        json_data = json.loads(self.dataSP)
        print(json_data.keys())

        criterios = json_data["criteriosVencimento"]
        print(criterios)

          # data_teste = '''
          #     {
          #         "primeiroNome": "Joao",
          #         "ultimoNome": "Smith",
          #         "idade": 25,
          #         "endereco": {
          #             "rua": "Rua Assis Brasil, 1000",
          #             "cidade": "Blumenau",
          #             "estado": "SC"
          #         },
          #         "telefones": [
          #             "5555-5555",
          #             "9999-9999"
          #         ],
          #         "emails": [
          #             {
          #                 "tipo": "pessoal",
          #                 "endereco": "joao@joao.com"
          #             },
          #             {
          #                 "tipo": "profissional",
          #                 "endereco": "joao.smith@algumaempresa.com"
          #             }
          #         ]
          #     }
          # '''




