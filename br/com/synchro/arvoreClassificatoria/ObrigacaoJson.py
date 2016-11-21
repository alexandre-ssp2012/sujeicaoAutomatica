import json


class ObrigacaoJson:

  def __init__(self):
      self.data = '''
                    {
                        "chave" : "obrigacaoPrincipal_1393459742240",
                        "nome" : "MG - PGTO ICMS ST",
                        "qualificacoes" : [
                            {
                                "chave" : "qualificacao_1",
                                "descricao" : "Qualificação 1",
                                "aplicabilidades" : [
                                    {
                                        "chave" : "aplicabilidade_1",
                                        "descricao" : "Refinaria de petróleo ou as suas bases em relação as operações interestaduais com GLGN de origem nacional e GLGN originado de importação."
                                    }
                                ],
                                "criteriosVencimento" : [
                                    {
                                        "chave" : "criterio_1",
                                        "descricao" : "Repasse - GLGN de origem nacional e GLGN originado de importação"
                                    }
                                ]
                            },
                            {
                                "chave" : "qualificacao_2",
                                "descricao" : "Qualificação 2",
                                "aplicabilidades" : [
                                    {
                                        "chave" : "aplicabilidade_2",
                                        "descricao" : "Estabelecimento industrial (operações precedentes) situado no Estado da Bahia, Mato Grosso do Sul, Rio de Janeiro, Santa Catarina,  Paraná, Rio de Janeiro ou de São Paulo, na condição de sujeito passivo por substituição nas operações interestaduais com alumínio em formas brutas, alumínio não ligado, ligas de alumínio, inclusive a granalha de alumínio e quaisquer outras mercadorias classificadas na posição NBM/SH 76.01 nas operação promovida por estabelecimento remetente mineiro que atenda, cumulativamente, aos requisitos descritos nas alíneas 'a', 'b', 'c', 'd' e 'e' do inciso II do artigo 125 da Parte 1 do Anexo XV do Decreto nº 43.080/002."
                                    },
                                    {
                                        "chave" : "aplicabilidade_2_1",
                                        "descricao" : "Estabelecimento industrial (operações precedentes) situado no Estado da Bahia, Paraná, Rio de Janeiro, São Paulo, Mato Grosso do Sul, Santa Catarina e o Distrito Federal, na condição de sujeito passivo por substituição nas operações interestaduais com alumínio em formas brutas, alumínio não ligado, ligas de alumínio, inclusive a granalha de alumínio e quaisquer outras mercadorias classificadas na posição NBM/SH 76.01, na hipótese de remessa de mercadoria para industrialização por conta e ordem do estabelecimento remetente mineiro."
                                    },
                                    {
                                        "chave" : "aplicabilidade_2_2",
                                        "descricao" : "Estabelecimento industrial (operações precedentes) destinatário localizado nos estados da Bahia, Paraná, Rio de Janeiro, São Paulo, Mato Grosso do Sul, Santa Catarina e o Distrito Federal, na condição de sujeito passivo por substituição, pela retenção e recolhimento do ICMS devido pela entrada decorrente de operação interestadual com alumínio em formas brutas, alumínio não ligado, ligas de alumínio, inclusive a granalha de alumínio e quaisquer outras mercadorias classificadas na posição NBM/SH 7601."
                                    },
                                    {
                                        "chave" : "aplicabilidade_2_3",
                                        "descricao" : "Estabelecimento industrial (operações precedentes) destinatário localizado nos estados da Bahia, Paraná, Rio de Janeiro, São Paulo, Mato Grosso do Sul, Santa Catarina e o Distrito Federal, na condição de sujeito passivo por substituição, pela retenção e recolhimento do ICMS devido pela entrada decorrente de operação interestadual com desperdícios e resíduos, inclusive a sucata, dos metais alumínio, cobre, níquel, chumbo, zinco e estanho e quaisquer outras mercadorias classificadas respectivamente nas subposições NBM/SH 7602.00, 7404.00, 7503.00, 7802.00, 7902.00, 8002.00."
                                    },
                                    {
                                        "chave" : "aplicabilidade_2_4",
                                        "descricao" : "Estabelecimento industrial situado no Estado da Bahia, Paraná, Rio de Janeiro ou de São Paulo, na condição de sujeito passivo por substituição, na hipótese de operação de remessa para industrialização por conta e ordem do remetente nem nas operações de transferência de alumínio em formas brutas, alumínio não ligado, ligas de alumínio, inclusive a granalha de alumínio e quaisquer outras mercadorias classificadas na posição NBM/SH 76.01."
                                    },
                                    {
                                        "chave" : "aplicabilidade_2_5",
                                        "descricao" : "Estabelecimento industrial situado no Estado da Bahia, Paraná, Rio de Janeiro ou de São Paulo, na condição de sujeito passivo por substituição, pela retenção e recolhimento do ICMS devido pela entrada decorrente de operação interestadual com alumínio em formas brutas, alumínio não ligado, ligas de alumínio, inclusive a granalha de alumínio e quaisquer outras mercadorias classificadas na posição NBM/SH 76.01."
                                    },
                                    {
                                        "chave" : "aplicabilidade_2_6",
                                        "descricao" : "Estabelecimento industrial situado no Estado da Bahia, Paraná, Rio de Janeiro ou de São Paulo, na condição de sujeito passivo por substituição, pela retenção e recolhimento do ICMS devido pela entrada decorrente de operação interestadual com desperdícios e resíduos, inclusive a sucata, dos metais cobre, níquel, chumbo, zinco, estanho e alumínio, e quaisquer outras mercadorias classificadas respectivamente nas subposições NBM/SH 7404.00, 7503.00, 7802.00, 7902.00, 8002.00, 7602.00."
                                    }
                                ],
                                "criteriosVencimento" : [
                                    {
                                        "chave" : "criterio_2",
                                        "descricao" : "Operações precedentes - Desperdícios/Resíduos/Sucatas e Alumínio em forma bruta"
                                    },
                                    {
                                        "chave" : "criterio_2_1",
                                        "descricao" : "Desperdícios/Resíduos e Alumínio em formas brutas"
                                    }
                                ]
                            },
                            {
                                "chave" : "qualificacao_3",
                                "descricao" : "Qualificação 3",
                                "aplicabilidades" : [
                                    {
                                        "chave" : "aplicabilidade_3",
                                        "descricao" : "CONAB, nas operações vinculadas ao Programa de Aquisição de Alimentos da Agricultura Familiar (PAA), relativamente ao imposto devido a título de substituição tributária, nas saídas internas promovidas por produtor rural."
                                    }
                                ],
                                "criteriosVencimento" : [
                                    {
                                        "chave" : "criterio_3",
                                        "descricao" : "CONAB"
                                    }
                                ]
                            },
                            {
                                "chave" : "qualificacao_4",
                                "descricao" : "Qualificação 4",
                                "aplicabilidades" : [
                                    {
                                        "chave" : "aplicabilidade_4",
                                        "descricao" : "Distribuidor hospitalar situado no Estado de Minas Gerais, na condição de sujeito passivo por substituição, pela retenção e recolhimento do ICMS devido nas operações subsequentes com as mercadorias submetidas ao regime de substituição tributária de que trata o capítulo 13 da Parte 2 do Anexo XV do RICMS (Medicamentos de uso humano e outros produtos farmacêuticos para uso humano ou veterinário)."
                                    },
                                    {
                                        "chave" : "aplicabilidade_4_1",
                                        "descricao" : "Distribuidor hospitalar situado em Minas Gerais nas operações subsequentes com as mercadorias de que trata o item 15 da Parte 2 do Anexo XV do RICMS."
                                    }
                                ],
                                "criteriosVencimento" : [
                                    {
                                        "chave" : "criterio_4",
                                        "descricao" : "Operações subsequentes (saídas)"
                                    }
                                ]
                            },
                            {
                                "chave" : "qualificacao_5",
                                "descricao" : "Qualificação 5",
                                "aplicabilidades" : [
                                    {
                                        "chave" : "aplicabilidade_5",
                                        "descricao" : "Estabelecimento comercializador de partes, componentes e acessórios, usados, de que trata o Capítulo 1 da Parte 2 do Anexo XV do RICMS, exceto em se tratando de recebimento em operação interestadual."
                                    },
                                    {
                                        "chave" : "aplicabilidade_5_1",
                                        "descricao" : "Estabelecimento comercializador de terminais portáteis de telefonia celular usados."
                                    },
                                    {
                                        "chave" : "aplicabilidade_5_2",
                                        "descricao" : "Estabelecimento comercializador de partes, componentes e acessórios de produtos autopropulsados, usados, de que trata o Capítulo 1 da Parte 2 do Anexo XV do RICMS, exceto em se tratando de recebimento em operação interestadual."
                                    }
                                ],
                                "criteriosVencimento" : [
                                    {
                                        "chave" : "criterio_5",
                                        "descricao" : "Autopeças USADOS (exceto em se tratando de recebimento em operação interestadual)"
                                    }
                                ]
                            },
                            {
                                "chave" : "qualificacao_6",
                                "descricao" : "Qualificação 6",
                                "aplicabilidades" : [
                                    {
                                        "chave" : "aplicabilidade_6",
                                        "descricao" : "Refinaria de petróleo ou as suas bases, em relação às operações com Combustíveis Derivados de Petróleo."
                                    },
                                    {
                                        "chave" : "aplicabilidade_6_1",
                                        "descricao" : "Refinaria ou suas bases, se constatada  a inexistência ou a insuficiência do valor recolhido, pela Diretoria de Gestão de Projetos da Superintendência de Fiscalização, em relação às operações cujo imposto relativo à gasolina “A” ou ao óleo diesel devesse ser retido por outros contribuintes."
                                    },
                                    {
                                        "chave" : "aplicabilidade_6_2",
                                        "descricao" : "Refinaria ou suas bases, se constatada pela Diretoria de Gestão de Projetos da Superintendência de Fiscalização a inexistência ou a insuficiência do valor do imposto recolhido."
                                    },
                                    {
                                        "chave" : "aplicabilidade_6_3",
                                        "descricao" : "Refinaria de petróleo ou suas bases, caso  não haja a manifestação prevista no inciso III do artigo 86 do Anexo XV do RICMS, em relação ao repasse do imposto provisionado, em favor da unidade federada para qual foi efetuado o provisionamento."
                                    }
                                ],
                                "criteriosVencimento" : [
                                    {
                                        "chave" : "criterio_6",
                                        "descricao" : "(Combustíveis derivados de petróleo) Provisão do ICMS retido anteriormente por outros contribuintes (provisão do valor do imposto devido às unidades federadas de destino das mercadorias, limitado ao valor efetivamente recolhido à unidade federada de origem)"
                                    },
                                    {
                                        "chave" : "criterio_6_1",
                                        "descricao" : "(Combustíveis derivados de petróleo) Repasse do ICMS retido anteriormente por refinaria de petróleo ou por suas bases (repasse do valor do imposto devido às unidades federadas de destino das mercadorias, limitado ao valor do imposto efetivamente retido e do relativo à operação própria, quando este Estado for destinatário da mercadoria)"
                                    },
                                    {
                                        "chave" : "criterio_6_2",
                                        "descricao" : "(Álcool Combustível e com Biodiesel B100) Provisão do ICMS anteriormente retido por Outros Contribuintes (em relação às operações cujo imposto relativo à gasolina “A” ou ao óleo diesel tenha sido anteriormente retido por outros contribuintes, a refinaria de petróleo ou suas bases deve efetuar a provisão do valor do imposto devido à unidade da Federação de origem do álcool etílico anidro combustível ou do biodiesel)"
                                    },
                                    {
                                        "chave" : "criterio_6_3",
                                        "descricao" : "(Álcool Combustível e com Biodiesel B100) Repasse do ICMS retido anteriormente pela Refinaria de Petróleo ou suas Bases (em relação às operações cujo imposto relativo à gasolina “A” ou ao óleo diesel tenha sido anteriormente retido pela própria refinaria de petróleo ou por suas bases, a refinaria de petróleo ou suas bases deve efetuar o  repasse do valor do imposto devido à unidade da Federação de origem do álcool etílico anidro combustível ou do biodiesel, quando o produto for originário deste Estado)"
                                    },
                                    {
                                        "chave" : "criterio_6_4",
                                        "descricao" : "(Álcool Combustível e com Biodiesel B100) Provisionamento do ICMS devido após comunicação da Sefaz pela não aceitação da dedução informada (valor provisionado ou a parcela referente ao valor contestado)"
                                    }
                                ]
                            }
                        ]
                    }'''

  def printJson(self):
      data = self.data
      json_data = json.loads(data)
      print(json_data.keys())
      print(json_data["chave"])
      print(json_data["nome"])
      print(json_data["qualificacoes"])

